# Password Strength Checker

A beginner-friendly Python command-line tool that gives local feedback on password strength. It does not store or transmit the password.

## Requirements

- Python 3.10 or newer
- Visual Studio Code (optional, with the Python extension)

## Run in VS Code

1. Open this project folder in VS Code.
2. Open the integrated terminal (**Terminal → New Terminal**).
3. Run:

   ```powershell
   python .\password_checker.py
   ```

4. Type a password at the hidden prompt and press Enter. (The characters are hidden while typing.)

To debug, open `password_checker.py`, click beside a line number to set a breakpoint, then press **F5** and select the **Password Checker** configuration. The integrated terminal will prompt for input.

On systems where `python` is not the Python 3 command, try `py -3 .\password_checker.py`.

## Project layout

```text
PasswordCheckerProject/
├── password_checker.py
├── .vscode/
│   └── launch.json
└── README.md
```

The existing `password_log.txt` folder is intentionally unused: saving passwords would put users at risk.

## Current limitations

This is a simple educational checker. It uses length and character variety heuristics plus a short common-password list. It is not a guarantee that a password is secure; using a password manager to generate a unique password or passphrase is recommended.

## GitHub

To publish this project, create an empty repository on GitHub, then connect it as the `origin` remote and push the project. The local folder does not currently have a Git repository or a GitHub remote.
