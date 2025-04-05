def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal

# Get user input
print("📈 Interest Calculator 📊")
principal = float(input("Enter Principal Amount (₹): "))
rate = float(input("Enter Interest Rate (%): "))
time = float(input("Enter Time (in years): "))

choice = input("Choose interest type (simple/compound): ").lower()

if choice == 'simple':
    si = simple_interest(principal, rate, time)
    print(f"\n💰 Simple Interest: ₹{si:.2f}")
    print(f"📦 Total Amount: ₹{principal + si:.2f}")
elif choice == 'compound':
    ci = compound_interest(principal, rate, time)
    print(f"\n💰 Compound Interest: ₹{ci:.2f}")
    print(f"📦 Total Amount: ₹{principal + ci:.2f}")
else:
    print("❌ Invalid choice! Please choose 'simple' or 'compound'.")
