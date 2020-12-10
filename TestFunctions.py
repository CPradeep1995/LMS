from Book import Book
from Catalog import Catalog
from User import User
from User import Member, Librarian

c = Catalog()
b1 = c.addBook('Politics of Opportunism','R P N Singh', '2019',100)
c.addBookItem(b1,'isbn1','R1')
c.addBookItem(b1,'isbn1-2','R1-2')
b2 = c.addBook('Malayalam poetry','Akkitham Achuthan Namboodri', '2019',130)
c.addBookItem(b2,'isbn2','R2')
b3 = c.addBook('Celestial Bodies','Jokha Alharthi', '2019',140)
c.addBookItem(b3,'isbn3','R3')

m = Member('member1','bangalore',24,'123412341234',25,c)
bi1 = m.issueBook('Politics of Opportunism')
bi2 = m.issueBook('Politics of Opportunism')
m.returnBook(bi1)
bi3 = m.issueBook('Politics of Opportunism')
bi4 = m.issueBook('Politics of Opportunism')