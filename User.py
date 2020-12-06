from Catalog import Catalog

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id

    def __repr__(self):
        return self.name
        

class Member(User):
    
    member_list=[]
    
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.books_issued=[]
        Member.member_list.append(self.name)
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    def issueBook(self,title,days=10):
        max_days=10
        self.days=days
        if 0 < self.days <= max_days:
            if title not in self.books_issued:
                val=False
                for book in Catalog.books:
                    if book.title == title:
                        if len(book.book_item) != 0:
                            book_item=book.book_item.pop()
                            book.total_count-=1
                            Catalog.addBookToIssued(title)
                            print("Book copy Issued Successfully for",self.days,"days.")
                            self.addBookToIssued(title,book_item)
                            val=True
                        else:
                            print("Book you are looking is not available")
                            val=True
                            break
                if val == False:
                    print("Requested book can't be found in library.")
                
            else:
                print("A copy of this book has already been issued by this member.")
        elif self.days <= 0:
            print("Please enter number of days more than '0'.")
        else:
            print("Can't issue book for more than ten days.")
            
    def addBookToIssued(self,title,book_item):
        self.books_issued.append((title,book_item))
        print(self.name,"has issued following books till now:")
        count=0
        for i in self.books_issued:
            count+=1
            print(count,".",i[0],i[1].isbn)
                    
                    
    def returnBook(self,isbn):
        print("Books currently issued by you:")
        count=0
        for i in self.books_issued:
            count+=1
            print(count,".",i[0],i[1].isbn)
        for book_item in self.books_issued:
            val=False
            if book_item[1].isbn == isbn:
                r_book_item=book_item[1]
                for book in Catalog.books:
                    if book == r_book_item.book:
                        book.book_item.append(r_book_item)
                        book.total_count += 1
                        print("Book item",r_book_item.isbn,"successfully returned.")
                        Catalog.issuedBooks.remove(r_book_item.book.title)
                        val=True
                self.books_issued.remove((r_book_item.book.title,r_book_item))
            if val == False:
                print("Sorry, you have not been issued any such book.")
        
        
class Librarian(User,Catalog):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        Catalog.__init__(self)
        
    def __repr__(self):
        return self.name + " " + self.location + " " + self.emp_id
    
    def addBook(self,title,author,publish_date,pages):
        Catalog._addBook(self,title, author, publish_date, pages)
        print(title,"added to catalog.")
    
    def addBookItem(self, title, isbn, rack):
        Catalog._addBookItem(self,title, isbn, rack)
        
    def displayAllBooks(self):
        Catalog.displayAllBooks(self)
        
    def removeBook(self, title):
        Catalog._removeBook(self,title)
    
    def removeBookItemFromCatalog(self,isbn):
        Catalog._removeBookItem(self,isbn)
