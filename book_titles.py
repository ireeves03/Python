def main():
    book_titles = []

    # Collect 10 book titles from the user
    while len(book_titles) < 10:
        title = input("Enter a book title: ")
        book_titles.append(title.title())

    # Create a sorted list
    sorted_titles = sorted(book_titles)

    # Display the titles
    for title in sorted_titles:
        print(title)

#Call the function
main()
