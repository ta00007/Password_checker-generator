# Password_checker-generator
# Password Strength Checker & Generator

A simple command-line Python tool that checks how strong a password is and estimates how long it would take to crack — plus a mode to generate a strong random password.

## Features

- **Password strength checker**
  - Detects commonly used weak passwords (e.g. `123456`, `password`, `qwerty`)
  - Calculates the character set used (lowercase, uppercase, digits, special characters)
  - Estimates total possible combinations based on password length and character variety
  - Shows estimated time to crack at different attack speeds:
    - 10 billion guesses/sec
    - 100 billion guesses/sec
    - 1 trillion guesses/sec
    - 100 trillion guesses/sec
  - Rates the password as Weak, Moderate, Strong, or Too Strong

- **Password generator**
  - Generates a random strong password of a user-specified length using letters, numbers, and special characters

## How to Run

```bash
python password_tool.py
```

You'll be prompted to enter a password to check. You can check multiple passwords, then optionally generate a new strong password at the end.

## Example

```
Enter the password: iloveyou
This password is TOO WEAK
Do you want to check another password? (y/n)
y
Enter the password: iamhere2026
Weak (Can be broken easily) -
 for 10 billion password attempts per second:
13,162,170 seconds, 219,370 minutes, 3,656 hours, 152 days, 0 years
 for 1 trillion password attempts per second:
1,316,217 seconds, 21,937 minutes, 366 hours, 15 days, 0 years
 for 100 trillion password attempts per second:
131,622 seconds, 2,194 minutes, 37 hours, 2 days, 0 years
 for 1 quadrillion password attempts per second:
1,316 seconds, 22 minutes, 0 hours, 0 days, 0 years
Do you want to check another password? (y/n)
n
If you want then I can create a strong password for you. Do you want me to create a strong password? (y/n)
y
Enter the length of the password: 16
Your strong password is: ys&f213EFjs71*$]
```
