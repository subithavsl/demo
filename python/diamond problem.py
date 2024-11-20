# Diamond problem in python 

class A:
  def display(self):
    print("Iam the display of class A")

class B(A):
  def display(self):
    print("Iam the display of class B")


class C(A):
  def display(self):
    print("Iam the display of class C")

class D(C,B):
  def display(self):
    print("Iam the display of class D")

o=D()
o.display()