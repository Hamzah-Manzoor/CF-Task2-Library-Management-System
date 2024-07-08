from admin import Admin


def main():
    admin = Admin()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Print Books")
        print("3. Search Books")
        print("4. Add User")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Print Borrowers")
        print("8. Print Users")
        print("9. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                book_id = int(input("Enter book ID: "))
                name = input("Enter book name: ")
                quantity = int(input("Enter quantity: "))
                admin.add_book(book_id, name, quantity)
            elif choice == '2':
                admin.print_books()
            elif choice == '3':
                prefix = input("Enter book name prefix: ")
                admin.search_books(prefix)
            elif choice == '4':
                user_id = int(input("Enter user ID: "))
                name = input("Enter user name: ")
                admin.add_user(user_id, name)
            elif choice == '5':
                user_id = int(input("Enter user ID: "))
                book_id = int(input("Enter book ID: "))
                admin.borrow_book(user_id, book_id)
            elif choice == '6':
                user_id = int(input("Enter user ID: "))
                book_id = int(input("Enter book ID: "))
                admin.return_book(user_id, book_id)
            elif choice == '7':
                admin.print_borrowers()
            elif choice == '8':
                admin.print_users()
            elif choice == '9':
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
