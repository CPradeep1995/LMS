class BookItem:
    def __init__(self,book,isbn,rack):
        self.book = book
        self.isbn = isbn
        self.rack = rack

    def __repr__(self):
        return self.isbn + ' ' + self.rack