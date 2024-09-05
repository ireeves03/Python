# Function to convert numeric grade to letter grade
def get_letter_grade(numeric_grade):
    if 90 <= numeric_grade <= 100:
        return 'A'
    elif 80 <= numeric_grade < 90:
        return 'B'
    elif 70 <= numeric_grade < 80:
        return 'C'
    elif 60 <= numeric_grade < 70:
        return 'D'
    else:
        return 'F'

 # Accept numeric grade from the user
numeric_grade = float(input("Enter your numeric grade: "))

# Ensure the grade is within the valid range
if 0 > numeric_grade > 100:
    print("Please enter a grade between 0 and 100.")
elif 0 <= numeric_grade <= 100:
# Get the letter grade
    letter_grade = get_letter_grade(numeric_grade)
print(f"Your letter grade is: {letter_grade}")
