class student:
  count=0

  def __init__(self, name, age):
    self.name=name
    self.age=age
    student.count += 1
    
  def printDetail(self):
    print("Name : ", self.name, " Age : ", self.age)
    

  @classmethod
  def total(cls):
    return cls.count
  
o = student("subi", 20)
o.printDetail()
print("Total Admission :", o.total())
a=student("vedha",21)
a.printDetail()
c=student("vedha",21)
c.printDetail()


print("Total Admission:", student.total())