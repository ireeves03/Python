# ask user to input integers
a= int(input("Enter an integer: "))
b= int(input("Enter another integer: "))

#and operator
if a > 0 and b > 0 :
    print("both numbers are greater than zero")
else:
    print("both numbers are not greater than zero")

if a > 100 and b > 100:
    print("both numbers are greater than 100")
else:
    print("both numbers are not greater than 100")

#or operator
if a % 2 == 0 or b % 2 == 0:
    print("either number is even")
else:
    print("neither number is even")
if a % 5 == 0 or b % 5 == 0:
    print("either number is divisible by 5")
else:
    print("neither number is divisible by 5")

#not operator
if not a > b:
    print(a, "is not greater than", b)

else:
    print(a, "is greater than", b)
if not a == b:
    print("both numbers are not equal")
else:
    print("both numbers are equal")