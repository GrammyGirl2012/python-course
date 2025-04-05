import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "❌ Password should be at least 8 characters long.\n"

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "❌ Add lowercase letters.\n"

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "❌ Add uppercase letters.\n"

    # Check for digits
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks += "❌ Add numbers.\n"

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks += "❌ Add special characters (e.g. !, @, #, etc).\n"

    # Strength level
    if strength == 5:
        return "✅ Strong password!", ""
    elif 3 <= strength < 5:
        return "⚠️ Medium strength password.", remarks
    else:
        return "❌ Weak password!", remarks

# Get password input from user
user_password = input("Enter your password: ")
strength_level, tips = check_password_strength(user_password)
print("\n" + strength_level)
if tips:
    print("Suggestions to improve:")
    print(tips)
