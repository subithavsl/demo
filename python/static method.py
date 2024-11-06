# static method in python

class student:
  def __init__(self, name, age):
    self.name=name
    self.age=age
    
  def printDetail(self):
    print("Name :", self.name, "Age :", self.age)
    
  @staticmethod
  def welcome():
    print("welcome to our institution")
  
  
s1=student("subi",20)
s1.printDetail()
s1.welcome()

s2=student("vedha",21)
s2.printDetail()
s2.welcome()