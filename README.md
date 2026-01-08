# Python Password Strength Checker

A simple command-line application that evaluates the strength of a password
based on common security rules.

This project was built to practice Python fundamentals such as:
- Functions
- Conditional logic
- Regular expressions
- Clean CLI input/output

## Features
- Checks password length
- Detects uppercase and lowercase letters
- Detects digits
- Detects special characters
- Classifies passwords as **Weak**, **Medium**, or **Strong**

## How It Works
The password is scored using five criteria:
1. Minimum length (8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character

The final strength is determined by the total score.

## How to Run
Make sure Python is installed, then run:

```bash
python password_checker.py


Example Output
=== Password Strength Checker ===
Enter your password: Hello@123
Password Strength: Strong


Author
Utkarsh