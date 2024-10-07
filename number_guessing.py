# using the random module
import random

# call the function to generate a random number between 1 and 100
random_number = random.randint(1,100)

#ask for user input and provide feedback
def main ():
    while True:
        try: 
            guess = int(input("Please guess a number between 1 and 100: "))
            difference = abs(guess - random_number)
            if difference == 0:
                print ("Congratulations! You've guessed the correct number!!")
                break
            elif difference <= 5:
                print ("Very Hot")
            elif difference <= 15:
                print ("Hot")
            elif difference <= 25:
                print ("Cool")
            else:
                print ("Cold")
        except ValueError:
            print ("Please enter a number between 1 and 100.")

main()