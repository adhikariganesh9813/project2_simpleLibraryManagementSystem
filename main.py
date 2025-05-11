# Simple library management system.....
class Book:
    def __init__ (self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.book_list.append(new_book)

    def display_books(self):
        available_books = [book for book in self.book_list if not book.is_borrowed]
        if not available_books:
            print("No available books in the library.")
        else:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")

    def borrow_book(self, title):
        for book in self.book_list:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You have borrowed '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' is already borrowed.")
                    return
        print("Book not found in the library")

    def return_book(self, title):
        for book in self.book_list:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"You have returned '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' was not borrowed.")
                    return
        print("Book not found in the library.")

# Interactive function to run my library system.... 
def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add a book")
        print("2. Display available books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = int(input("Enter you choice (1-5): "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title,author)

        elif choice == 2:
            library.display_books()

        elif choice == 3:
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)

        elif choice == 4:
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1 to 5.")

main()

    

