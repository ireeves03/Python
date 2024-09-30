# Global constants for conversion
POUNDS_TO_KG = 0.453592
INCHES_TO_METERS = 0.0254

def main():
    # Ask the user for weight in pounds and height in inches
    pounds = int(input("Enter your weight in pounds: "))
    inches = int(input("Enter your height in inches: "))

    # Conversion to Metric
    kg = pounds * POUNDS_TO_KG
    meters = inches * INCHES_TO_METERS

    # BMI Calculation
    bmi = calculate_bmi(kg, meters)
    if bmi < 0:
        print ("please enter positive integers.")
 # Display the calculated BMI and BMI category
    else:
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Your BMI category is: {categorize_bmi(bmi)}")

def calculate_bmi(weight, height):
    #calculate BMI using metric units.
    return weight / (height ** 2)

def categorize_bmi(bmi):
    #categorize BMI.
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


main()
