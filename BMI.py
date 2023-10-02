def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)
while True:
    try:
        weight_kg = float(input("Enter your weight in kilograms: "))
        height_m = float(input("Enter your height in meters: "))

        if weight_kg <= 0 or height_m <= 0:
            raise ValueError("Weight and height must be positive values.")

        break
    except ValueError as e:
        print(f"Error: {e}")
bmi = calculate_bmi(weight_kg, height_m)
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
else:
    category = "Overweight"
print(f"Your BMI is: {bmi:.2f}")
print(f"You are in the {category} category.")