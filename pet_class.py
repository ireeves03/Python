class Pet:
    # Class variable for veterinary office name
    vet_name = "Happy Paws Veterinary Clinic"
    
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self._owner_first_name = owner_first_name
        self._owner_last_name = owner_last_name
        self._pet_id = pet_id
        self._pet_name = pet_name
        self._pet_type = pet_type

    # Accessor (getter) methods
    def get_owner_first_name(self):
        return self._owner_first_name
    
    def get_owner_last_name(self):
        return self._owner_last_name
    
    def get_pet_id(self):
        return self._pet_id
    
    def get_pet_name(self):
        return self._pet_name
    
    def get_pet_type(self):
        return self._pet_type
    
    # Mutator (setter) methods
    def set_owner_first_name(self, first_name):
        self._owner_first_name = first_name
    
    def set_owner_last_name(self, last_name):
        self._owner_last_name = last_name
    
    def set_pet_id(self, pet_id):
        self._pet_id = pet_id
    
    def set_pet_name(self, pet_name):
        self._pet_name = pet_name
    
    def set_pet_type(self, pet_type):
        self._pet_type = pet_type
    
    # Method to display pet information
    def display_pet_info(self):
        print(f"Owner's First Name: {self.get_owner_first_name()}")
        print(f"Owner's Last Name: {self.get_owner_last_name()}")
        print(f"Pet ID: {self.get_pet_id()}")
        print(f"Pet Name: {self.get_pet_name()}")
        print(f"Pet Type: {self.get_pet_type()}")
        print(f"Veterinary Clinic: {Pet.vet_name}")
        print("")

# Function to check if a property exists in a pet object
def check_property(pet, property_name):
    return hasattr(pet, property_name)

def main():
    # Create three instances of Pet
    pet1 = Pet("John", "Doe", 101, "Buddy")
    pet2 = Pet("Jane", "Smith", 102, "Mittens", "Cat")
    pet3 = Pet("Alice", "Johnson", 103, "Rex", "Dog")
    
    # Show the use of setter methods
    pet1.set_pet_name("Buddy Updated")
    pet2.set_pet_type("Updated Cat")

    # Display information for each pet
    print("Pet 1 Information:")
    pet1.display_pet_info()

    print("Pet 2 Information:")
    pet2.display_pet_info()

    print("Pet 3 Information:")
    pet3.display_pet_info()

    # Check properties
    print(f"Does pet1 have 'owner_first_name' property? {check_property(pet1, '_owner_first_name')}")
    print(f"Does pet2 have 'pet_id' property? {check_property(pet2, '_pet_id')}")
    print(f"Does pet3 have 'color' property? {check_property(pet3, 'color')}")

main()
