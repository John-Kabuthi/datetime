def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    try:
        year = int(input("Enter a year: "))

        if year <= 0:
            raise ValueError("Year must be a positive number.")

        break
    except ValueError as e:
        print(f"Error: {e}")
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")