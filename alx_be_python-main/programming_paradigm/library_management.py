
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = True
    

class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book: Book):
        self._books.append(book)

    def list_available_books(self):
        for b in Library._books:
            b: Book
            if b.__is_checked_out:
                print(f"{b.title} by {b.author}")

    def check_out_book(self, title):
        for b in Library._books:
            b: Book
            if b.title == title:
                b.__is_checked_out = False

    def return_book(self):
        for b in Library.__books:
            b: Book
            if b.title == title:
                b.__is_checked_out = True

