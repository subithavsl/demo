# init method in python

class user:
  def __init__(self,name):
    print("call when new instance created")

    self.name=name 
    
  def printall(self):
    print("name:",self.name)
    
o1=user("subitha")
o1.printall()
o2=user("subi")
o2.printall()
