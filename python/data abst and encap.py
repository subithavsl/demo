# Abstraction and Encapsulation in python:

class Library:
  def __init__(self, books):
    self.books=books
    
  def list_books(self):
    print("Available books")
    for book in self.books:
      print(book)
  
  def borrow_book(self, borrow_book):
    if borrow_book in self.books:
      print("get your book now")
      self.books.remove(borrow_book)
    else:
      print("book not available")
      
  def receive_book(self, receive_book):
    print("You have returned the book")
    self.books.append(receive_book)
    
books=['c','c++','java']
o=Library(books)
  
msg="""
    1.Display book
    2.Borrow book
    3.Return book
"""

while True:
    print(msg)
    ch=int(input("Enter your choice:"))
    if ch==1:
      o.list_books()
    elif ch==2:
      book=input("Enter book name to borrow:")
      o.borrow_book(book)
    elif ch==3:
      book=input("Enter book name to return:")
      o.receive_book(book)
    else:
      print("Thankyou come again")
      quit()