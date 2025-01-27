import os
import subprocess
import customtkinter as ctk
from pathlib import Path

class SSHKeyGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SSH Key Wizard for GitHub")
        self._setup_ui()
        self.ssh_dir = Path.home() / ".ssh"
        
    def _setup_ui(self):
        # Email Input
        ctk.CTkLabel(self, text="GitHub Email:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = ctk.CTkEntry(self, width=300)
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)

        # Key Type Selection
        ctk.CTkLabel(self, text="Key Type:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.key_type = ctk.CTkComboBox(self, values=["ed25519", "rsa-4096"])
        self.key_type.grid(row=1, column=1, padx=10, pady=5)
        self.key_type.set("ed25519")

        # Filename Input
        ctk.CTkLabel(self, text="Key Filename:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.filename_entry = ctk.CTkEntry(self, width=300, placeholder_text="id_github")
        self.filename_entry.grid(row=2, column=1, padx=10, pady=5)

        # Passphrase
        ctk.CTkLabel(self, text="Passphrase (optional):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.passphrase_entry = ctk.CTkEntry(self, width=300, show="•")
        self.passphrase_entry.grid(row=3, column=1, padx=10, pady=5)

        # ssh-agent Toggle
        self.ssh_agent_toggle = ctk.CTkCheckBox(self, text="Add key to ssh-agent")
        self.ssh_agent_toggle.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Generate Button
        generate_btn = ctk.CTkButton(self, text="Generate Key", command=self._generate_key)
        generate_btn.grid(row=5, column=1, padx=10, pady=20, sticky="e")

    def _generate_key(self):
        email = self.email_entry.get().strip()
        key_type = self.key_type.get()
        filename = self.filename_entry.get().strip() or f"id_github_{key_type}"
        passphrase = self.passphrase_entry.get().strip()

        # Ensure .ssh directory exists
        self.ssh_dir.mkdir(exist_ok=True, mode=0o700)

        # Build ssh-keygen command
        key_path = self.ssh_dir / filename
        if key_type == "ed25519":
            cmd = f'ssh-keygen -t ed25519 -C "{email}" -f "{key_path}" -N "{passphrase}"'
        else:
            cmd = f'ssh-keygen -t rsa -b 4096 -C "{email}" -f "{key_path}" -N "{passphrase}"'

        # Execute command
        try:
            subprocess.run(cmd, shell=True, check=True)
            os.chmod(key_path, 0o600)  # Secure private key
        except subprocess.CalledProcessError as e:
            self._show_error(f"Key generation failed: {str(e)}")
            return

        # Add to ssh-agent if requested
        if self.ssh_agent_toggle.get():
            subprocess.run(f'eval "$(ssh-agent -s)" && ssh-add {key_path}', shell=True)

        # Display public key
        public_key = (key_path.with_suffix(".pub")).read_text()
        self._show_public_key(public_key)

    def _show_public_key(self, key: str):
        window = ctk.CTkToplevel(self)
        window.title("Public Key for GitHub")
        textbox = ctk.CTkTextbox(window, width=600, height=150)
        textbox.insert("1.0", key)
        textbox.configure(state="disabled")
        textbox.pack(padx=20, pady=20)

    def _show_error(self, message: str):
        ctk.CTkLabel(self, text=message, text_color="red").grid(row=6, column=1, pady=10)

if __name__ == "__main__":
    app = SSHKeyGenerator()
    app.mainloop()