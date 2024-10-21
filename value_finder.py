# Defining main function
def main():
    #ask for user input
    user_input = input("Please enter a character: ")
    #loop to validate input
    while len(user_input) != 1:
        print ("Please enter exactly one character.")
        user_input = input("Enter a character: ")
    else:
        #convert to ascii value 
        ascii_value = ord(user_input)
    print(f"The ASCII value of {user_input} is {ascii_value}")

#call function
main()