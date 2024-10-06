# PRODIGY_CS_03: Password Complexity Checker

Welcome To Mr Srinivas's Password Complexity Checker Tool!
The Password Complexity Checker is a Python-based program that helps users evaluate the strength of a password by analyzing key components such as:

- Length of the password (minimum of 8 characters)
- Checking Wether uppercase and lowercase letters are added or not?
- Presence of Digits
- Usage of special characters (e.g., @, #, $)

The program provides feedback on how strong or weak the password is, which can help users improve their password security and avoid common vulnerabilities. This tool is designed to ensure basic security requirements and protect against password-based attacks.

# Features

- User Instructions: Clear guidelines on how to create a strong and secure password.
- Password Evaluation: The password is evaluated against five key criteria and classified as Strong, Moderate, or Weak.

# Working of the Tool

The tool checks the password strength based on the following conditions:

1. Password length of 8 or more characters.

2. Presence of lowercase letters.

3. Presence of uppercase letters.

4. Use of at least one digit.

5. Use of at least one special character (like @, #, $, etc.).

If all conditions are met, the password is classified as Strong. If it meets 3-4 conditions, it's Moderate, and less than 3 conditions indicate a Weak password.

# Procedure

1. Install Python 3.x if not already installed.
2. Download or clone the repository:
```bash
https://github.com/mr-srinivas14/PRODIGY_CS_03.git
```
3. Navigate to the Downloded Directory
```bash
cd PRODIGY_CS_03
```
4. Run the File
```bash
python3 Password_Strength_Checker.py
```
# Example
```bash

  ___                                     _    ___                    _            _  _            ___  _              _             
 | _ \ __ _  ___ _____ __ __ ___  _ _  __| |  / __| ___  _ __   _ __ | | ___ __ __(_)| |_  _  _   / __|| |_   ___  __ | |__ ___  _ _ 
 |  _// _` |(_-<(_-<\ V  V // _ \| '_|/ _` | | (__ / _ \| '  \ | '_ \| |/ -_)\ \ /| ||  _|| || | | (__ | ' \ / -_)/ _|| / // -_)| '_|
 |_|  \__,_|/__//__/ \_/\_/ \___/|_|  \__,_|  \___|\___/|_|_|_|| .__/|_|\___|/_\_\|_| \__| \_, |  \___||_||_|\___|\__||_\_\___||_|  
                                                               |_|                         |__/                                      
    
================================================================================
Welcome to the Mr Srinivas's Password Complexity Checker Tool!
Please Follow the following steps to make your password stronger:
- Password must be at least 8 characters long.
- Use both uppercase and lowercase letters.
- Use numbers and special characters (e.g., @, #, $, etc.).
================================================================================
Enter a password to check its strength: MrSrinivas@1234
Password Strength: Strong
Criteria Feedback:
Length: Meets
Uppercase letters: Meets
Lowercase letters: Meets
Digits: Meets
Special characters: Meets

Thanks For Using This Tool
```
# Credits
- Developed by Mr Srinivas
