from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Adjust if birthday hasn't occurred yet this year
    if days < 0:
        months -= 1
        days += 30  # Approximation
    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# Get user input
print("🎂 Age Calculator")
dob_input = input("Enter your birth date (YYYY-MM-DD): ")

try:
    birth_date = datetime.strptime(dob_input, "%Y-%m-%d")
    years, months, days = calculate_age(birth_date)
    print(f"\n🧮 You are {years} years, {months} months, and {days} days old.")
except ValueError:
    print("❌ Invalid date format! Please use YYYY-MM-DD.")
2