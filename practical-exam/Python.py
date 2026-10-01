    # ==========================================
# BILL SPLITTER & TIP CALCULATOR
# Practical Exam - 1
# ==========================================

print("==========================================")
print("       Welcome to the Bill Splitter App!")
print("==========================================")

while True:

    # 1. User Inputs
    bill = float(input("Enter total bill amount: "))
    people = int(input("Enter number of people: "))

    # 2. Validate number of people
    if people <= 0:
        print("Error: Number of people must be greater than 0.")
        continue

    # Tip percentage
    tip_percent = int(input("Enter tip percentage (0/5/10/15/20): "))

    # 3. Validate tip percentage
    if tip_percent not in (0, 5, 10, 15, 20):
        print("Error: Invalid tip percentage.")
        continue

    # 4. Calculations
    tip_amount = (tip_percent / 100) * bill
    total_bill = bill + tip_amount
    per_person = total_bill / people

    # 5. Display results
    print()
    print("------------------------------------------")
    print(f"Tip Amount: ₹{tip_amount:.2f}")
    print(f"Total Bill (with Tip): ₹{total_bill:.2f}")
    print(f"Each person should pay: ₹{per_person:.2f}")
    print("------------------------------------------")

    # 6. Repeat the process
    choice = input("Would you like to calculate another bill? (y/n): ")

    if choice.lower() != "y":
        break

print()
print("Thank you for using the Bill Splitter App!")
print("==========================================")