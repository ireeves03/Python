# Class definition for a Person
class Person:
    def __init__(self, name, address, age, phone_number):
        self._name = name
        self._address = address
        self._age = age
        self._phone_number = phone_number

    # Accessor methods (getters)
    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_age(self):
        return self._age

    def get_phone_number(self):
        return self._phone_number

    # Mutator methods (setters)
    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_age(self, age):
        self._age = age

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    # Method to display information
    def display_info(self):
        print(f"Name: {self.get_name()}")
        print(f"Address: {self.get_address()}")
        print(f"Age: {self.get_age()}")
        print(f"Phone Number: {self.get_phone_number()}")
        print("")

def main():
    # Create three instances of Person
    person1 = Person("Bella Reeves", "123 Main St, Crystal Lake, IL", 21, "815-555-1234")
    person2 = Person("Daniel Reeves", "456 Maple Ave, McHenry, IL", 25, "815-445-5678")
    person3 = Person("Kittrix Reeves", "789 Elm St, Johnsburg, IL", 18, "815-905-9012")

    # Display information for each person
    print("Person 1 Information:")
    person1.display_info()

    print("Person 2 Information:")
    person2.display_info()

    print("Person 3 Information:")
    person3.display_info()

main()

    