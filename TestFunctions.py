from Book import Book
from Catalog import Catalog
from User import User
from User import Member, Librarian

# b1 = Book('Shoe Dog','Phil Knight', '2015',312)
# b1.addBookItem('123hg','H1B2')
# b1.addBookItem('124hg','H1B3')

# b1.printBook()

catalog = Catalog()

b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
print(b)
catalog.addBookItem(b, '123hg','H1B2')
catalog.addBookItem(b, '123hg','H1B4')
catalog.addBookItem(b, '123hg','H1B5')

b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017', 318)
catalog.addBookItem(b, '463hg','K1B2')
print(b)

# catalog.displayAllBooks()

# m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')

# librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 
# print (m1)
# print (librarian)

# b = catalog.searchByName('Shoe Dog')
# print (b)


# catalog.removeBookItem('Shoe Dog','124hg')
# catalog.displayAllBooks()
#m1.issueBook

# b1 = Book('two states','Chetan Bhagath', '2015',312)
# b1.addBookItem('123hg','R1')
# b1.printBook()
# print(b1.searchBookItem('123hg'))
# print(b1.removeBookItem(b1))
# b2 = Book('three states','Chetan', '2016',300)
# b2.addBookItem('124hg','R2')
# b2.printBook()
# print(b2.searchBookItem('124hg'))

user = User('pradeep','bangalore','25','789478957895')
print(user)

mem = Member('pradeep','bangalore','25','789478957895','123')
print(mem)

mem = Member('sandeep','bangalore','20','124578895623','526')
print(mem)
