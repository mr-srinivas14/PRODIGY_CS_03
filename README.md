# PRODIGY_CS_03: Password Complexity Checker

The Password Complexity Checker is a Python-based program that helps users evaluate the strength of a password by analyzing key components such as:

Length of the password (minimum of 8 characters)
Inclusion of uppercase and lowercase letters
Presence of numbers
Use of special characters (e.g., @, #, $) The program provides feedback on how strong or weak the password is, which can help users improve their password security and avoid common vulnerabilities. This tool is designed to ensure basic security requirements and protect against password-based attacks.

# Features

- User Instructions: Clear guidelines on how to create a strong and secure password.
- Password Evaluation: The password is evaluated against five key criteria and classified as Strong, Moderate, or Weak.
- Exit Command: Users can exit the tool easily by typing 'E', 'e', 'Exit', or 'exit'.

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
git clone https://github.com/mr-srinivas14/PRODIGY_CS_03.git
```
3. Navigate to the Downloded Directory
```bash
cd PRODIGY_CS_03
```
4. Run the File
```bash
python3 password_checker.py
```
# Example
```bash

  ___                                     _    ___                    _            _  _            ___  _              _             
 | _ \ __ _  ___ _____ __ __ ___  _ _  __| |  / __| ___  _ __   _ __ | | ___ __ __(_)| |_  _  _   / __|| |_   ___  __ | |__ ___  _ _ 
 |  _// _` |(_-<(_-<\ V  V // _ \| '_|/ _` | | (__ / _ \| '  \ | '_ \| |/ -_)\ \ /| ||  _|| || | | (__ | ' \ / -_)/ _|| / // -_)| '_|
 |_|  \__,_|/__//__/ \_/\_/ \___/|_|  \__,_|  \___|\___/|_|_|_|| .__/|_|\___|/_\_\|_| \__| \_, |  \___||_||_|\___|\__||_\_\___||_|  
                                                               |_|                         |__/                                      
    
================================================================================
Welcome to the Mr Srinivas's Password Complexity Checker! Tool
Follow the guidelines below to create a strong password:
- Password must be at least 8 characters long.
- Include both uppercase and lowercase letters.
- Include numbers and special characters (e.g., @, #, $, etc.).
To exit the program, type 'E', 'e', 'Exit', or 'exit'.
================================================================================
Enter a password to check its strength (or type 'E', 'e', 'Exit', or 'exit' to quit): Github@15092024
Password strength: Strong
================================================================================
Enter a password to check its strength (or type 'E', 'e', 'Exit', or 'exit' to quit): e
Exiting the program. Goodbye!
```
# Credits
- Developed by Mr Srinivas
