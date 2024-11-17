class Pet:
    def __init__(self, kind, breed, name):
        self._kind = kind
        self._breed = breed
        self._name = name

    # Getters
    def get_kind(self):
        return self._kind

    def get_breed(self):
        return self._breed

    def get_name(self):
        return self._name

    # Setters
    def set_kind(self, kind):
        self._kind = kind

    def set_breed(self, breed):
        self._breed = breed

    def set_name(self, name):
        self._name = name

    # Method to print details of the pet
    def print_details(self):
        print(f"Kind: {self.get_kind()}")
        print(f"Breed: {self.get_breed()}")
        print(f"Name: {self.get_name()}")
        print("")

def main():
    # Create three instances of Pet
    pet1 = Pet("Dog", "Golden Retriever", "Buddy")
    pet2 = Pet("Cat", "Siamese", "Whiskers")
    pet3 = Pet("Bird", "Parakeet", "Joe")

    # Call the print_details method for each pet
    print("Pet 1 Details:")
    pet1.print_details()

    print("Pet 2 Details:")
    pet2.print_details()

    print("Pet 3 Details:")
    pet3.print_details()

    # Demonstrate a special method or function
    print(f"pet3's breed using getattr: {getattr(pet3, '_breed')}")
    


main()
