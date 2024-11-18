class NotNumericError(Exception):
    pass

def get_number_from_user():
    while True:
        try:
            user_input = input("Please enter a number: ")
            if not user_input.isnumeric():
                raise NotNumericError(f"'{user_input}' is not a number.")
            else:
                print(f"'{user_input}' is a valid number.")
                break
        except NotNumericError as e:
            print(f"Error: {e}")
        finally:
            print("End of program execution attempt.\n")

def main():
    get_number_from_user()

if __name__ == "__main__":
    main()
