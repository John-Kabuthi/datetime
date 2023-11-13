#KABUTHI JOHN MUTISYA
#SCT211-0055/2022
#PROGRAMMING LANGUAGES ASSIGNMENT(EXCEPTION HANDLING)


class LeapYearCheck:
    def __init__(self, year):
        self.year = year

    def is_leap_year(self):
        if(self.year %4==0):
            return True
        else:
            return False
        
if __name__ == "__main__":
    while True:
        try:
            year=int(input("Enter a year: "))

            if year<=0:
                raise ValueError("year must be positive number")
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    year_check = LeapYearCheck(year)

    if year_check.is_leap_year():
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year.")
    