
# SSH Key Wizard for GitHub 🗝️

A simple GUI tool for Linux users to create SSH keys, save them securely, and get your public key ready for GitHub – no terminal commands needed!

![SSH Key Wizard Screenshot](screenshot.png) <!-- Add a screenshot of your GUI here -->

## What Does This Tool Do? ✨

- 🔒 **Create SSH Keys**: Generates private/public key pairs (using GitHub’s recommended security settings).
- 📂 **Auto-Save to `.ssh`**: Saves keys directly to your `~/.ssh` folder with proper permissions.
- 📋 **Copy-Paste Public Key**: Shows your public key in a popup for easy GitHub setup.
- 🛡️ **Security First**: Optional passphrases and `ssh-agent` integration.

Perfect for developers new to GitHub or SSH who want to avoid manual terminal steps!

---

## How to Use It 🖱️

### Step 1: Install Dependencies
You’ll need:
- Python 3.8+
- `customtkinter` (GUI library)
- `tkinter` (usually pre-installed on Linux)

**Terminal Commands:**
```bash
# Install Python (if missing)
sudo apt install python3 python3-pip  # Debian/Ubuntu
# or
sudo dnf install python3 python3-pip  # Fedora

# Install CustomTkinter
pip3 install customtkinter
```

### Step 2: Run the Program
Download the script (`ssh_key_wizard.py`) and run:
```bash
python3 ssh_key_wizard.py
```

### Step 3: Fill in the Form
1. **Email**: Enter your GitHub account email.
2. **Key Type**: Keep `ed25519` (recommended) or choose `rsa-4096`.
3. **Filename**: Name your key (e.g., `id_github`). Leave blank for a default name.
4. **Passphrase**: Optional extra security (like a password for your key).
5. **Add to ssh-agent**: Check this to avoid typing your passphrase repeatedly.

![Filled Form Example](form_example.png) <!-- Add example screenshot -->

### Step 4: Copy Your Public Key 🔑
After clicking "Generate Key":
- A popup will show your **public key**.
- Copy the entire text (it starts with `ssh-ed25519...` or `ssh-rsa...`).

### Step 5: Add to GitHub
1. Go to [GitHub SSH Keys Settings](https://github.com/settings/keys).
2. Click **New SSH Key**, paste your public key, and save.

---

## Security Notes 🔐
- 🔑 Your private key is saved to `~/.ssh/[filename]` with strict permissions (only you can read it).
- ❗ Never share your private key (`id_github` file) with anyone!
- 🔔 Using a passphrase? Remember it – GitHub will ask for it when pushing/pulling code.

---

## Troubleshooting 🛠️
**Error: "ModuleNotFoundError"**  
Run `pip3 install customtkinter` if you skipped Step 1.

**Key not working with GitHub?**  
- Ensure you copied the **public** key (ends with `.pub`).
- Double-check your email matches your GitHub account.

**Permission issues?**  
Run:
```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_*  # Replace with your key filename
```

---

## FAQ ❓
**Q: Why Linux only?**  
The tool uses Linux-specific file permissions and `ssh-agent` integration. Windows/macOS users can follow [GitHub’s SSH guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)(plus im not a big developer so im pretty sure im the only one who uses my applications lol).

**Q: Should I use `ed25519` or `rsa-4096`?**  
Use `ed25519` (modern and secure). Only pick `rsa-4096` if working with older systems.

**Q: Do I need a passphrase?**  
Optional, but recommended for sensitive accounts. However, i did have a yubikey already tied to my pc. I might need to change this because im pretty sure the passphrases were phased out.

**Q: What’s `ssh-agent` for?**  
It remembers your passphrase so you don’t type it every time.

---

## License 📄
MIT License - free to use and modify. Always verify code from untrusted sources!

---

Made with ❤️ by Junior Ducatel.  
Credits: [GitHub Docs](https://docs.github.com/) | [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

