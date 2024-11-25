def main():
    try:
        # Open the file sales_totals in read mode
        with open("sales_totals.txt", "r") as file:
            total = 0.0
            count = 0
            
            # Read in all the lines using a loop
            for line in file:
                # Strip newline symbol and convert each line to a float
                number = float(line.strip())
                # Add each number to the running total
                total += number
                # Count the number of lines
                count += 1
                # Format and display each number
                print(f"Sales amount: ${number:.2f}")
            
            # Outside of the loop, format and display the total, the count, and the average
            print(f"\nTotal sales: ${total:.2f}")
            print(f"Number of sales entries: {count}")
            if count > 0:
                average = total / count
                print(f"Average sales: ${average:.2f}")
            else:
                print("No sales entries found.")

    except FileNotFoundError:
        print("Error: The file 'sales_totals.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


main()
