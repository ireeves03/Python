# import necessary modules
import calendar
import datetime

def main():
        #get current year
        current_year = datetime.datetime.now().year

        # ask user for birth month
        birth_month_input = input("Please enter your birth month (1-12): ")

        # Validate user input
        birth_month = int(birth_month_input)
        if birth_month < 1 or birth_month > 12:
            raise ValueError("Month must be between 1 and 12")

        #generate calendar for month
        user_calendar = calendar.month(current_year, birth_month)

        #print output
        print(f"\nCalendar for {calendar.month_name[birth_month]} {current_year}:\n")
        print (user_calendar)

main()