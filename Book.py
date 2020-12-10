from BookItem import BookItem

class Book:
    def __init__(self,name,author,publish_date,pages):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0
        self.book_item = []
        
    def addBookItem(self,isbn,rack):
        b = BookItem(self,isbn,rack)
        self.book_item.append(b)
        self.total_count +=1
        return b

    def printBook(self):
        for book_item in self.book_item:
            print (book_item.isbn)
        print(self.book_item)
            
    def searchBookItem(self,isbn):
        for book_item in self.book_item:
            if isbn.strip() == book_item.isbn:
                return book_item
            
    def removeBookItem(self,book_item):
        if book_item in self.book_item:
            self.book_item.remove(book_item)
            self.total_count -=1
    
    def getBookItem(self):
        if self.total_count > 0:
            return self.book_item[0]

    def __repr__(self):
        return self.name
