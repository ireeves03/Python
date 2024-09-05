# Determining what a user can do based on their age.
age = float(input("How old are you? "))
if age >= 16:
    print("\nYou are old enough to drive.")
elif age < 16:
    print("\nYou are not old enough to drive.")
if age >= 18:
    print("You are old enough to vote.")
elif age < 18:
    print("You are not old enough to vote.")
if age >= 21:
    print("You can buy alcohol.")
elif age < 21:
    print("You cannot buy alcohol.")
if age >= 65:
    print("You are eligible for a senior discount.")
elif age < 65:
    print("You are not eligible for a senior discount.")