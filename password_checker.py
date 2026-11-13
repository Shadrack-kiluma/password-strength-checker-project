"""A small, privacy-friendly password strength checker."""

from getpass import getpass
import re


COMMON_PASSWORDS = {
    "123456", "123456789", "password", "password123", "qwerty",
    "letmein", "admin", "welcome", "iloveyou",
}

PASSWORD_RULES = {
    "length": r".{8,}",
    "uppercase": r"[A-Z]",
    "lowercase": r"[a-z]",
    "digit": r"\d",
    "special": r"[!@#$%^&*(),.?\":{}|<>]",
}

RULE_FEEDBACK = {
    "length": "Use at least 8 characters; 12 or more is better.",
    "uppercase": "Add an uppercase letter.",
    "lowercase": "Add a lowercase letter.",
    "digit": "Add a number.",
    "special": "Add a symbol, such as ! or #.",
}


def assess_password(password: str) -> tuple[str, list[str]]:
    """Return a strength label and actionable feedback for a password."""
    feedback: list[str] = []
    score = 0

    for rule, regex in PASSWORD_RULES.items():
        if re.search(regex, password):
            score += 1
        else:
            feedback.append(RULE_FEEDBACK[rule])

    if password.lower() in COMMON_PASSWORDS:
        return "Very weak", ["This is a commonly used password. Choose a unique passphrase."]

    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    if not feedback:
        feedback.append("Good foundation. A unique passphrase is even better.")
    return strength, feedback


def check_strength(password: str) -> str:
    """Return only the strength label, matching the original project function."""
    return assess_password(password)[0]


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
