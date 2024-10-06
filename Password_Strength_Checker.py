import re

def print_header():
    header = """
  ___                                     _    ___                    _            _  _            ___  _              _             
 | _ \ __ _  ___ _____ __ __ ___  _ _  __| |  / __| ___  _ __   _ __ | | ___ __ __(_)| |_  _  _   / __|| |_   ___  __ | |__ ___  _ _ 
 |  _// _` |(_-<(_-<\ V  V // _ \| '_|/ _` | | (__ / _ \| '  \ | '_ \| |/ -_)\ \ /| ||  _|| || | | (__ | ' \ / -_)/ _|| / // -_)| '_|
 |_|  \__,_|/__//__/ \_/\_/ \___/|_|  \__,_|  \___|\___/|_|_|_|| .__/|_|\___|/_\_\|_| \__| \_, |  \___||_||_|\___|\__||_\_\\___||_|  
                                                               |_|                         |__/                                      
    """
    print(header)
    print("="*80)
    print("Welcome to the Mr Srinivas's Password Complexity Checker Tool!")
    print("Please Follow the following steps to make your password stronger:")
    print("- Password must be at least 8 characters long.")
    print("- Use both uppercase and lowercase letters.")
    print("- Use numbers and special characters (e.g., @, #, $, etc.).")
    print("="*80)

def password_strength_checker(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    strength_score = sum([
        length_criteria,
        upper_criteria,
        lower_criteria,
        digit_criteria,
        special_char_criteria
    ])

    strength = ""
    if strength_score < 3:
        strength = "Weak"
    elif strength_score == 3:
        strength = "Moderate"
    else:
        strength = "Strong"

    feedback = {
        "Length": "Meets" if length_criteria else "Does not meet",
        "Uppercase letters": "Meets" if upper_criteria else "Does not meet",
        "Lowercase letters": "Meets" if lower_criteria else "Does not meet",
        "Digits": "Meets" if digit_criteria else "Does not meet",
        "Special characters": "Meets" if special_char_criteria else "Does not meet",
    }

    return strength, feedback

def main():
    print_header()
    password = input("Enter a password to check its strength: ")
    strength, feedback = password_strength_checker(password)

    print(f"Password Strength: {strength}")
    print("Criteria Feedback:")
    for criteria, result in feedback.items():
        print(f"{criteria}: {result}")
    print("Thanks For Using This Tool")

if __name__ == "__main__":
    main()
