"""A small, privacy-friendly password strength checker."""

from getpass import getpass
import re


COMMON_PASSWORDS = {
    "123456", "123456789", "password", "password123", "qwerty",
    "letmein", "admin", "welcome", "iloveyou",
}


def assess_password(password: str) -> tuple[str, list[str]]:
    """Return a strength label and actionable feedback for a password."""
    feedback: list[str] = []
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Use at least 12 characters for better protection.")
    else:
        feedback.append("Use at least 8 characters; 12 or more is better.")

    checks = [
        (r"[a-z]", "Add a lowercase letter."),
        (r"[A-Z]", "Add an uppercase letter."),
        (r"\d", "Add a number."),
        (r"[^A-Za-z0-9]", "Add a symbol, such as ! or #."),
    ]
    for pattern, suggestion in checks:
        if re.search(pattern, password):
            score += 1
        else:
            feedback.append(suggestion)

    if password.lower() in COMMON_PASSWORDS:
        return "Very weak", ["This is a commonly used password. Choose a unique passphrase."]

    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    if not feedback:
        feedback.append("Good foundation. A unique passphrase is even better.")
    return strength, feedback


def main() -> None:
    print("Password Strength Checker")
    print("Your password is checked locally and is never saved.\n")
    password = getpass("Enter a password to check: ")
    if not password:
        print("Please enter a non-empty password.")
        return

    strength, feedback = assess_password(password)
    print(f"\nStrength: {strength}")
    for item in feedback:
        print(f"- {item}")


if __name__ == "__main__":
    main()
