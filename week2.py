#Book tracker CLI
import json
import os
BOOK_FILE = "books.json"

def load_books():
    if os.path.exists(BOOK_FILE):
        with open(BOOK_FILE, "r") as f:
            return json.load(f)
    else:
        return []
    
def save_books(books):
    with open(BOOK_FILE, "w") as f:
        json.dump(books, f)    
    
books = load_books()

def add_book():
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    
    if title.strip() == "" or author.strip() == "":
        print("Title and Author cannot be empty.")
        return

    try:
        pages = int(input("Enter # of pages: "))
    except ValueError:
        print("Pages must be a number.")
        return

    newBook = {
        "title": title,
        "author": author,
        "pages": pages
    }

    books.append(newBook)
    save_books(books)
    print("Book added and saved successfully!")

def print_books():
    for book in books:
        print(f'{book["title"]} by {book["author"]} - {book["pages"]} pages')

def total_pages():
    total = sum(book["pages"] for book in books)
    return total

def delete_book_by_title():
    title = input("Enter the title of the book to delete: ")

    if title.strip() == "":
        print("Title cannot be empty.")
        return
    
    for book in books:
        if book["title"] == title:
            books.remove(book)
            print(f'Book {book["title"]} has been deleted')
            save_books(books)
            return
    else:
        print("Book not Found")
        return        

# Main menu
while True:
    print("\nPress 1 to add a book")
    print("Press 2 to view books")
    print("Press 3 to show total pages")
    print("Press 4 to delete book by title")
    print("Press 5 to Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        print_books()
    elif choice == "3":
        print(f"Total pages: {total_pages()}")
    elif choice == "4":
        delete_book_by_title()    
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")