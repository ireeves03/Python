def main():
    # Prompt the user to enter the current date and time, and a diary entry
    date_time = input("Enter the current date and time (e.g., 2024-11-25 14:30): ")
    diary_entry = input("Enter your diary entry: ")

    # Open or create the file diary.txt in append mode
    with open("diary/diary.txt", "a") as diary_file:
        diary_file.write(f"Date and Time: {date_time}\n")
        diary_file.write(f"Entry: {diary_entry}\n")
        diary_file.write("\n")  # Blank line to separate entries


    # Confirm the entry has been added
    print("Your diary entry has been saved.")

# Run the main function
main()
