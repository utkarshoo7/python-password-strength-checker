"""
Password Strength Checker (CLI)

Checks password strength based on:
- Length
- Uppercase letters
- Lowercase letters
- Digits
- Special characters
"""

import re


def check_password_strength(password: str) -> str:
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase letter
    if re.search(r"[a-z]", password):
        score += 1

    # Digit
    if re.search(r"[0-9]", password):
        score += 1

    # Special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"


def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ").strip()

    if not password:
        print("Password cannot be empty.")
        return

    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")


if __name__ == "__main__":
    main()
