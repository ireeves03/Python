# list available seats to user
def display_available_seats(seats):
    print("\nAvailable seats: ", seats)

# prompt user for seat purchase
def purchase_ticket(seats):
    while True:
        display_available_seats(seats)
        seat_number = int(input("\nEnter the seat number you want to purchase (or 0 to finish): "))
        
        if seat_number == 0:
            break
        elif seat_number in seats:
            seats.remove(seat_number)
            print(f"\nSeat {seat_number} has been successfully purchased.")
        else:
            print("\nInvalid seat number or seat already taken. Please try again.")

def main():
    seats = list(range(1, 21))  # Initialize the seating list with seat numbers 1 to 20
    purchase_ticket(seats)
    print("\nThank you for your purchase!")

if __name__ == "__main__":
    main()

