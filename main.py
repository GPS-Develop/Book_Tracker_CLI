import book  # this is your book.py file

books = book.load_books()
while True:
    print("\nPress 1 to add a book")
    print("Press 2 to view books")
    print("Press 3 to show total pages")
    print("Press 4 to delete a book by title")
    print("Press 5 to quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book.add_book(books)   
    elif choice == "2":
        book.print_books(books)
    elif choice == "3":
        print(f"Total pages: {book.total_pages(books)}")
    elif choice == "4":
        book.delete_book_by_title(books)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")
        