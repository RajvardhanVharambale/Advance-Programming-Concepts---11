class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
b1 = Book(1, "Python Basics", "John", 300)
b2 = Book(2, "Java Programming", "James", 400)
b3 = Book(3, "Data Structures", "Robert", 500)
b1.display()
print()
b2.display()
print()
b3.display()