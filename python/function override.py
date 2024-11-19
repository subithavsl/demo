# function overriding in python:

class Employee:
  def workinghrs(self):
    self.hrs=50
   
  def printhrs(self):
    print("Total working hrs: ", self.hrs)


class Trainee(Employee):
  def workinghrs(self):
    self.hrs=60
    
  def resethrs(self):
    super().workinghrs()
    # (super() is a inbuild function in python it is used to refer the base class )
    
    
employee=Employee()
employee.workinghrs()
employee.printhrs()

trainee=Trainee()
trainee.workinghrs()
trainee.printhrs()

#reset trainee hrs

trainee.resethrs()
trainee.printhrs()