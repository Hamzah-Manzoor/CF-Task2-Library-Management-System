from admin import Admin


def main():
    admin = Admin()

    while True:
        print("""
            Library Management System
            1. Add Book
            2. Print Books
            3. Search Books
            4. Add User
            5. Borrow Book
            6. Return Book
            7. Print Borrowers
            8. Print Users
            9. Exit
        """)

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                admin.add_book()
            elif choice == '2':
                admin.print_books()
            elif choice == '3':
                admin.search_books()
            elif choice == '4':
                admin.add_user()
            elif choice == '5':
                admin.borrow_book()
            elif choice == '6':
                admin.return_book()
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
