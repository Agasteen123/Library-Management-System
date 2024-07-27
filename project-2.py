class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"Title: {self.title}, Author: {self.author}, Status: {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" by {book.author} added to the library.')

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f'You have borrowed "{book.title}".')
                return
        print(f'Sorry, "{title}" is not available.')

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f'You have returned "{book.title}".')
                return
        print(f'"{title}" was not borrowed from this library.')

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            book = Book(title, author)
            library.add_book(book)
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            title = input("Enter the book title to borrow: ")
            library.borrow_book(title)
        elif choice == "4":
            title = input("Enter the book title to return: ")
            library.return_book(title)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
