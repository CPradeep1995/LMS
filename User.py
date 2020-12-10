class User:
    def __init__(self, name, location, age, aadhar_id,catalog):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        self.catalog = catalog

class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id,catalog):
        super().__init__(name, location, age, aadhar_id,catalog)
        self.student_id = student_id
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    def issueBook(self,name,days=10):
        iss_book = self.catalog.searchByName(name)
        if iss_book is None or iss_book.total_count==0:
            print("requested book not available")
        else:
            book_item = iss_book.getBookItem()
            self.catalog.removeBookItem(iss_book.name, book_item.isbn)
            print('requested book issued')
            return book_item
    
    def returnBook(self, book_item):
        self.catalog.addBookItem(book_item.book,book_item.isbn,book_item.rack)
        print('book is returned successfully')
        
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id,catalog)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    def addBook(self,name,author,publish_date,pages):
        self.catalog.addBook(name,author,publish_date,pages)
    
    def removeBook(self,name):
        self.catalog.removeBook(name)
    
    def removeBookItemFromCatalog(self,catalog,book,isbn):
        if catalog.searchByName(book.name):
            catalog.removeBookItem(book.name,isbn)