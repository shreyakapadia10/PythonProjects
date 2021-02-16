class Library:
    def __init__(self, book_list, library_name):
        self.book_list = book_list
        self.library_name = library_name
        self.lend_books = {}

    def show_books(self):
        if not self.book_list:
            print('No Books are available.')
        else:
            print('Available Books are: ')
            for index, book in enumerate(self.book_list):
                print(f'{index+1}. {book}')

    def add_book(self, book_name):
        self.book_list.append(book_name)

    def lend_book(self, book_name, person_name):
        if book_name not in self.book_list and book_name not in self.lend_books:
            print('Please check the book name again!')
        elif book_name not in self.book_list and book_name in self.lend_books:
            owner_name = self.lend_books.get(book_name)
            print(f"The {book_name} is not available now, it is lended by {owner_name}")
        else:
            self.lend_books[book_name] = person_name
            self.book_list.remove(book_name)
            print(f"The Book '{book_name}' is successfully lend to {person_name}!")

    def return_book(self, book_name):
        try:
            del self.lend_books[book_name]
            self.add_book(book_name)
            print(f"The Book {book_name} is successfully returned!")
        except LookupError:
            print('Please check the book name again!')


if __name__ == '__main__':
    lib = Library(['BlackBook', 'Object Oriented Programming', 'Python Programming'], "Shreya's Library")
    while True:
        print('Press \n1. To See Available Books \t2. To Lend Book \t3. To Add Book \t4. To Return Book \t5. To Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            lib.show_books()
        elif choice == 2:
            bookName = input("Please Enter Book Name: ")
            ownerName = input("Please Enter Your Name: ")
            bookName = bookName.title()
            ownerName = ownerName.title()
            print('Checking for book availability...')
            lib.lend_book(bookName, ownerName)
        elif choice == 3:
            bookName = input("Please Enter Book Name: ")
            bookName = bookName.title()
            lib.add_book(bookName)
        elif choice == 4:
            bookName = input("Please Enter Book Name: ")
            bookName = bookName.title()
            lib.return_book(bookName)
        elif choice == 5:
            break
        else:
            print('Invalid Choice!')
print('Thank you for using the Library Management System! Have a nice day!')