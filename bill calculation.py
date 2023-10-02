def total_per_person(total_bill, tip_percentage, num_people):
    total_tip = total_bill * (tip_percentage / 100)
    total_amount = total_bill + total_tip
    per_person_amount = total_amount / num_people
    return per_person_amount

while True:
    try:
        total_bill = float(input("Enter the total bill amount: $"))
        tip_percentage_option = int(input("Choose a tip percentage option (10, 12, or 15): "))
        num_people = int(input("Enter the number of people splitting the bill: "))

        if tip_percentage_option not in [10, 12, 15]:
            raise ValueError("Invalid tip percentage option. Please choose 10, 12, or 15.")

        if total_bill <= 0 or num_people <= 0:
            raise ValueError("Total bill amount and number of people must be positive.")

        break
    except ValueError as e:
        print(f"Error: {e}")

total_per_person = total_per_person(total_bill, tip_percentage_option, num_people)
print(f"Each person should pay: ${total_per_person:.2f}")