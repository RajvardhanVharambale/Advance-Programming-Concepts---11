def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")

    file = open("books.txt", "a")

    file.write(book_id + "," + title + "," + author + ",Available\n")

    file.close()

    print("Book added successfully.")


def search_book():
    book_id = input("Enter Book ID to search: ")

    file = open("books.txt", "r")

    found = False

    for line in file:

        data = line.strip().split(",")

        if data[0] == book_id:
            print("\nBook Found")
            print("ID:", data[0])
            print("Title:", data[1])
            print("Author:", data[2])
            print("Status:", data[3])

            found = True
            break

    file.close()

    if not found:
        print("Book not found.")


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    file = open("books.txt", "r")

    lines = file.readlines()

    file.close()

    found = False

    for i in range(len(lines)):

        data = lines[i].strip().split(",")

        if data[0] == book_id:

            found = True

            if data[3] == "Available":
                data[3] = "Issued"

                lines[i] = ",".join(data) + "\n"

                print("Book issued successfully.")

            else:
                print("Book is already issued.")

            break

    file = open("books.txt", "w")

    file.writelines(lines)

    file.close()

    if not found:
        print("Book not found.")


def return_book():
    book_id = input("Enter Book ID to return: ")

    file = open("books.txt", "r")

    lines = file.readlines()

    file.close()

    found = False

    for i in range(len(lines)):

        data = lines[i].strip().split(",")

        if data[0] == book_id:

            found = True

            data[3] = "Available"

            lines[i] = ",".join(data) + "\n"

            print("Book returned successfully.")

            break

    file = open("books.txt", "w")

    file.writelines(lines)

    file.close()

    if not found:
        print("Book not found.")


def display_available_books():

    file = open("books.txt", "r")

    print("\nAvailable Books:")

    for line in file:

        data = line.strip().split(",")

        if data[3] == "Available":
            print(data[0], data[1], data[2])

    file.close()


while True:

    print("\n===== BOOK MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        search_book()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        display_available_books()

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")