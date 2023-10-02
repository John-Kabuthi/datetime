from datetime import datetime
year_of_birth = int(input("Enter your year of birth (YYYY): "))
month_of_birth=int(input("Enter your month of birth: "))
day_of_birth=int(input("Enter your day of birth: "))
current_date = datetime.now()
age_in_years = current_date.year - year_of_birth
age_in_months = current_date.month - current_date.month
age_in_days = current_date.day - current_date.day
if current_date.month < month_of_birth or (current_date.month == month_of_birth and current_date.day < day_of_birth):
    age_in_years -= 1
print(f"Your age is {age_in_years} years, {age_in_months} months, and {age_in_days} days.")