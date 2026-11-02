# Python Password Strength Checker

A small command-line Python project that classifies a password using five simple character-based checks. It was created to practise functions, conditional logic, regular expressions, and terminal input/output.

> **Important:** This is an educational heuristic, not a security-grade password-strength estimator. It does not measure password entropy, detect breached passwords, or account for common password patterns.

## Checks performed

The current implementation awards one point for each condition:

1. Password length is at least 8 characters.
2. At least one uppercase letter is present.
3. At least one lowercase letter is present.
4. At least one digit is present.
5. At least one character from the script's configured special-character set is present.

The score is mapped to a label:

| Score | Label |
|---:|---|
| 0–2 | Weak |
| 3–4 | Medium |
| 5 | Strong |

These labels describe only the script's rule score. They should not be interpreted as a guarantee that a password is difficult to guess.

## Requirements

- Python 3.8 or newer
- No third-party packages required (uses Python's built-in `re` module)

## Run

Clone the repository:

```bash
git clone https://github.com/utkarshoo7/python-password-strength-checker.git
cd python-password-strength-checker
```

Run the checker:

```bash
python password_checker.py
```

## Example

```text
=== Password Strength Checker ===
Enter your password: Hello@123
Password Strength: Strong
```

The example shows the output format; it is not a security recommendation to reuse that password.

## Current limitations

- Uses a fixed set of five character checks.
- Does not estimate entropy or guessability.
- Does not check against known compromised-password lists.
- Uses a simple score-to-label mapping.
- The current command-line input method should not be treated as secure secret entry.

## Possible improvements

- Add automated tests for empty input and score boundaries.
- Expand the heuristic documentation and special-character handling.
- Use hidden terminal input for local interactive use.
- Consider a well-reviewed password-strength estimator for any real security application.

## Author

**Utkarsh Chougule**
