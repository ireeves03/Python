def main():
    # Create tuple with class names
    programming_classes = ('\nIntro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals')
    
    # For loop to print each class 
    for course in programming_classes:
        print(course)
    
    # Print number of classes in the tuple
    print(f"\nI will need to take {len(programming_classes)} classes.")

# Call main function
main()
