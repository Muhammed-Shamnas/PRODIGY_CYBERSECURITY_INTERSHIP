import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check the length of the password
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine the strength level
    if strength == 5:
        strength_level = "Strong"
    elif strength >= 3:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"

    return strength_level, feedback

def main():
    while True:
        password = input("Enter a password to assess (or 'exit' to quit): ")
        if password.lower() == 'exit':
            break

        strength_level, feedback = assess_password_strength(password)
        print(f"Password Strength: {strength_level}")
        if feedback:
            print("Feedback:")
            for tip in feedback:
                print(f"- {tip}")

if __name__ == "__main__":
    main()
