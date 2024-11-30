from datetime import datetime

def main():
    # Print blank lines for better readability in the terminal
    print("\n\n")
    try:
        # Get the current date and time
        today = datetime.today()
        
        # Prompt the user for their birth year, month, and day
        birth_year = int(input("What year were you born?  "))
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
        
        # Create a datetime object for the birthday
        birthday = datetime(birth_year, month, day)
        
        # Print the formatted birthday
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 

        # Calculate the difference in days between today and the birthday
        delta = today - birthday
        print(f'Difference is {delta.days} days')

        # Calculate the age in years by dividing the difference in days by 365.2425 to account for leap years
        delta_years = delta.days // 365.2425
        print(f'You are {delta_years} years old')
       
    except Exception as e:
        # Print any exception that occurs
        print(f"ooooops!!!:  {e}") 
        # Call the main function again to prompt the user for input
        main()

# Run the main function
main()
