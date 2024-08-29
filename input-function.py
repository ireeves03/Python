#asking user to input budget and expenses
budget = float(input("enter total budget: "))
housing = float(input("enter amount spent on housing: "))
utilities = float(input("enter amount spent on utilites: "))
groceries = float(input("enter amount spent on groceries: "))
transportation = float (input("enter amount spent on transportation: "))
health = float (input ("enter amount spent on health care: "))
personal = float (input("enter amount spent on personal care: "))
clothing = float (input("enter amount spent on clothing: "))
debt = float (input("enter amount spent on debt: "))

#calculating percent of budget spent
percent1 = (housing / budget) * 100 
percent2 = (utilities / budget) * 100 
percent3 = (groceries / budget) * 100 
percent4 = (transportation / budget) * 100 
percent5 = (health / budget) * 100 
percent6 = (personal / budget) * 100 
percent7 = (clothing / budget) * 100 
percent8 = (debt / budget) * 100 

#output of percentages to user
print(f"\nThe total budget is {budget}")
print(f"Percent of total budget spent on housing is {percent1}% ")
print(f"Percent of total budget spent on utilities is {percent2}% ")
print(f"Percent of total budget spent on groceries is {percent3}% ")
print(f"Percent of total budget spent on transportation is {percent4}% ")
print(f"Percent of total budget spent on health care is {percent5}% ")
print(f"Percent of total budget spent on personal care is {percent6}% ")
print(f"Percent of total budget spent on clothing is {percent7}% ")
print(f"Percent of total budget spent on debt is {percent8}% ")
print()