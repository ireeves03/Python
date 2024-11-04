
def is_between_8_and_20(password):
    length_of_password = len(password)
    if length_of_password<8 or length_of_password>20:
        return False
    else:
        return True

def has_one_uppercase(password):
    for char in password:
      if char.isupper():
        return True
    return False

def has_one_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False

def has_one_number(password):
    for char in password:
        if char.isnumeric():
            return True
    return False

def has_one_symbol(password):
    for char in password:
        if not char.isalnum():
            return True
    return False




def main():
    while True:
            user_input = input("Enter a password: ")
            length = is_between_8_and_20(user_input)
            upper = has_one_uppercase(user_input)
            lower = has_one_lowercase(user_input)
            number = has_one_number(user_input)
            symbol = has_one_symbol(user_input)
            if not length or not upper or not lower or not number or not symbol:
                print("Doesn't meet criteria. Try again")
            else:
                confirm_password = input("Re-enter the password to confirm: ")
                if user_input == confirm_password:
                    print("Password set successfully!")
                    break
                else:
                    print("Passwords do not match. Try again")
        
            
main()