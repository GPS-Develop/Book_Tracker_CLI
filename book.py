import json
import os

BOOK_FILE = "books.json"

def load_books():
    if os.path.exists(BOOK_FILE):
        with open(BOOK_FILE, "r") as f:
            return json.load(f)
    return []

def save_books(books):
    with open(BOOK_FILE, "w") as f:
        json.dump(books, f)

def add_book(books):
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

    new_book = {
        "title": title,
        "author": author,
        "pages": pages
    }

    books.append(new_book)
    save_books(books)
    print("Book added and saved successfully!")

def print_books(books):
    for book in books:
        print(f'{book["title"]} by {book["author"]} - {book["pages"]} pages')

def total_pages(books):
    return sum(book["pages"] for book in books)

def delete_book_by_title(books):
    title = input("Enter the title of the book to delete: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    for book in books:
        if book["title"] == title:
            books.remove(book)
            save_books(books)
            print(f'Book "{title}" has been deleted.')
            return
    print("Book not found.")