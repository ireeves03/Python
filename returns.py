#defining function
def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest
principal = float(input("What is the principal amount?: "))
rate = float(input("What is the rate of interest?: "))
time = float(input("how long will the money be invested/borrowed?(in years): "))

#calling the function
calculate_interest(principal, rate, time)

calculated_interest = calculate_interest(principal, rate, time)
print(f"The simple interest for a principal amount of ${principal:,.2f} \nat an interest rate of {rate}% \nover a period of {time} years is:  ${calculated_interest:,.2f}")