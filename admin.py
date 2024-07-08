import os
import json
from book import Book
from user import User


class Admin:
    def __init__(self, books_file='books.txt',
                 users_file='users.txt',
                 borrows_file='borrows.txt'):
        """
        Initialize the admin class to manage books, users,
        and borrowing activities.

        :param books_file: str: File to store book data
        :param users_file: str: File to store user data
        :param borrows_file: str: File to store borrow data
        """
        self.books_file = books_file
        self.users_file = users_file
        self.borrows_file = borrows_file

        self.books = self.load_data(self.books_file, Book)
        self.users = self.load_data(self.users_file, User)
        self.borrowed_books = self.load_data(self.borrows_file, dict)

    def load_data(self, filename, data_type):
        """
        Load data from a file using JSON.

        :param filename: str: The name of the file to read from
        :param data_type: type: The type of data to load (Book, User, or dict)
        :return: dict: The data read from the file
        """
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                if data_type == dict:
                    return {
                        int(key): value
                        for key, value
                        in json.load(file).items()
                    }
                data = json.load(file)
                return {
                    int(key): data_type(**value)
                    for key, value
                    in data.items()
                }
        return {}

    def save_data(self, filename, data):
        """
        Save data to a file using JSON.

        :param filename: str: The name of the file to write to
        :param data: dict: The data to write to the file
        """
        with open(filename, 'w') as file:
            if isinstance(data, dict) and all(isinstance(v, (Book, User)) for v in data.values()):
                json.dump({k: v.__dict__ for k, v in data.items()}, file)
            else:
                json.dump(data, file)

    def add_book(self):
        """
        Add a new book to the library.
        """
        # book_id, name, quantity = None, None, None
        try:
            book_id = int(input("Enter book ID: "))
            name = input("Enter book name: ")
            quantity = int(input("Enter quantity: "))
        except ValueError as e:
            print(f"Invalid input: {e}")
            return

        if book_id in self.books:
            print("Book ID already exists.")
            return
        book = Book(id=book_id, name=name, quantity=quantity)
        self.books[book_id] = book
        self.save_data(self.books_file, self.books)
        print(f"Added book: {book}")

    def print_books(self):
        """Print all available books in the library."""
        for book in self.books.values():
            print(book)

    def search_books(self):
        """
        Search for books by name using a prefix.
        """

        try:
            prefix = input("Enter book name prefix: ")
        except ValueError as e:
            print(f"Invalid input: {e}")
            return

        found_books = [
            book for book in self.books.values()
            if book.name.startswith(prefix)
        ]
        for book in found_books:
            print(book)

    def add_user(self):
        """
        Add a new user to the system.
        """
        try:
            user_id = int(input("Enter user ID: "))
            name = input("Enter user name: ")
        except ValueError as e:
            print(f"Invalid input: {e}")
            return

        if user_id in self.users:
            print("User ID already exists.")
            return
        user = User(id=user_id, name=name)
        self.users[user_id] = user
        self.save_data(self.users_file, self.users)
        print(f"Added user: {user}")

    def borrow_book(self):
        """
        Borrow a book from the library.
        """

        try:
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
        except ValueError as e:
            print(f"Invalid input: {e}")
            return

        if user_id not in self.users:
            print("User ID does not exist.")
            return
        if book_id not in self.books:
            print("Book ID does not exist.")
            return
        book = self.books[book_id]
        if book.quantity <= 0:
            print("Book is not available.")
            return

        book.quantity -= 1
        if user_id not in self.borrowed_books:
            self.borrowed_books[user_id] = []
        self.borrowed_books[user_id].append(book_id)
        self.save_data(self.books_file, self.books)
        self.save_data(self.borrows_file, self.borrowed_books)
        print(f"Book borrowed: {book}")

    def return_book(self):
        """
        Return a borrowed book to the library.
        """

        try:
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
        except ValueError as e:
            print(f"Invalid input: {e}")
            return

        if user_id not in self.borrowed_books or book_id not in self.borrowed_books[user_id]:
            print("No record of this book being borrowed by this user.")
            return

        book = self.books[book_id]
        book.quantity += 1
        self.borrowed_books[user_id].remove(book_id)
        self.save_data(self.books_file, self.books)
        self.save_data(self.borrows_file, self.borrowed_books)
        print(f"Book returned: {book}")

    def print_borrowers(self):
        """Print users who borrowed books and their borrowed books."""
        for user_id, book_ids in self.borrowed_books.items():
            user = self.users[user_id]
            books = [self.books[book_id] for book_id in book_ids]
            print(f"{user} borrowed {[str(book) for book in books]}")

    def print_users(self):
        """Print all users in the system."""
        for user in self.users.values():
            print(user)
