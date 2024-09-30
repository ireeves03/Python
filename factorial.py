#Defining Factorial Function
def factorial (n):
    if n <= 1 :
        return 1
    else: 
        return n * (n-1)
    
#Defining Main Function
def main ():
    n = int(input("Please enter a positive integer: "))
    result = factorial(n)
    print(f"The factorial of {n} is {result}")

#Calling the function
main()