
def main_menu():
    print("Menu:")
    while True:
        try:
            print("\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")

def check():
    try:
        file = open("customer_list.txt", 'r')
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []

def create():
    customer = check()
    fname = input("Please enter the customer's first name: ")
    lname = input("Please enter the customer's last name: ")
    phone = input("Please enter the customer's phone: ")
    email = input("Please enter the customer's email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customer.append(entry)
    save(customer)

def save(output):
    file = open("customer_list.txt", 'w')
    for line in output:
        file.write(line)
    file.close()
    print("File updated.")

def read():
    customer = check()
    lname = input("Please enter the last name of the customer: ")
    found = False
    for entry in customer:
        if lname in entry:
            print(f"Entry found: {entry}")
            found = True
            break
    if not found:
        print("No entry found with that last name.")

def update():
    customer = check()
    lname = input("Please enter the last name of the customer to update: ")
    for i, entry in enumerate(customer):
        if lname in entry:
            print(f"Current entry: {entry}")
            fname = input("Please enter the new first name: ")
            lname = input("Please enter the new last name: ")
            phone = input("Please enter the new phone: ")
            email = input("Please enter the new email: ")
            updated_entry = f"{fname}, {lname}, {phone}, {email}\n"
            customer[i] = updated_entry
            save(customer)
            return
    print("No entry found with that last name.")

def delete():
    customer = check()
    lname = input("Please enter the last name of the customer to delete: ")
    for i, entry in enumerate(customer):
        if lname in entry:
            print(f"Current entry: {entry}")
            confirm = input("Are you sure you want to delete this entry? (yes/no): ")
            if confirm.lower() == 'yes':
                del customer[i]
                save(customer)
                return
    print("No entry found with that last name.")


choice = main_menu()
if choice == 1:
            create()
elif choice == 2:
            read()
elif choice == 3:
            update()
elif choice == 4:
            delete()
elif choice == 5:
            print("Quitting...")

main_menu()