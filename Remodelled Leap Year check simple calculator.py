#KABUTHI JOHN MUTISYA
#SCT211-0055/2022
#PROGRAMMING LANGUAGES ASSIGNMENT(CLASSES)

#class creation

class Leap_Year_Check:
    def __init__(self, year):
        self.year = year

        #Checking whether it is a leap year
        
    def is_leap_year(self):
        if (self.year % 4 == 0):
            return True
        else:
            return False
if __name__ == "__main__":
    while True:
        try:
            year = int(input("Enter a year:"))

            #ensuring the year is positive

            if year <= 0:
                raise ValueError("Year must be a positive number.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    year_check = Leap_Year_Check(year)

    #Checking whether it is a leap year using the Leap_Year_Check class

    if year_check.is_leap_year():
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")