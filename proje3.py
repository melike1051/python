class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def book_list(self):
        self.file.seek(0)
        file_content = self.file.read()
        file_lines = file_content.splitlines()
        for line in file_lines:
            book_details = line.split(',')
            print(f"Book: {book_details[0]}, Author: {book_details[1]}")

    def add_book(self):
        name = input("Please enter book name:")
        author = input("Please enter author name:")
        year = input("Please enter release year:")
        page = input("Please enter page number:")
        book_details = f"{name},{author},{year},{page}\n"
        self.file.write(book_details)
        print("Book added successfully")

    def remove_book(self):
     title = input("Enter the title of the book you want to remove: ")
     self.file.seek(0)
     books = self.file.readlines()
     new_books = [book for book in books if title not in book]
     if len(books) == len(new_books):
        print(f"Book not found.")
     else:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(new_books)
            print(f"Book removed successfully.")


       

       

lib = Library()

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("Q) Exit")

    choice = input("Please enter your choice:")
    if choice == '1':
        lib.book_list()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == 'Q':
        print("Exit")
        break
    else:
        print("Please enter a number between 1 and 4.")
