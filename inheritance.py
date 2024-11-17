class Employee:
    def __init__(self, name, employee_number):
        self._name = name
        self._employee_number = employee_number

    # Accessor methods (getters)
    def get_name(self):
        return self._name

    def get_employee_number(self):
        return self._employee_number

    # Mutator methods (setters)
    def set_name(self, name):
        self._name = name

    def set_employee_number(self, employee_number):
        self._employee_number = employee_number

class ProductionWorker(Employee):
    def __init__(self, name, employee_number, shift_number, hourly_pay_rate):
        super().__init__(name, employee_number)
        self._shift_number = shift_number
        self._hourly_pay_rate = hourly_pay_rate

    # Accessor methods (getters)
    def get_shift_number(self):
        return self._shift_number

    def get_hourly_pay_rate(self):
        return self._hourly_pay_rate

    # Mutator methods (setters)
    def set_shift_number(self, shift_number):
        self._shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self._hourly_pay_rate = hourly_pay_rate

def main():
    # Prompt user for ProductionWorker details
    name = input("Enter the employee's name: ")
    employee_number = input("Enter the employee number: ")
    shift_number = int(input("Enter the shift number (1 for day, 2 for night): "))
    hourly_pay_rate = float(input("Enter the hourly pay rate: "))

    # Create an instance of ProductionWorker
    worker = ProductionWorker(name, employee_number, shift_number, hourly_pay_rate)

    # Display the data using the object's methods
    print("\nProduction Worker Details:")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_employee_number()}")
    print(f"Shift Number: {worker.get_shift_number()}")
    print(f"Hourly Pay Rate: ${worker.get_hourly_pay_rate():.2f}")

if __name__ == "__main__":
    main()
