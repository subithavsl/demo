# Multiple inheritance in python :

class father:
  def fishing(self):
    print("fishing in Rivers")
    
  def chess(self):
    print("playing chess from father")

class mother:
  def cooking(self):
    print("cooking food")
    
  def chess(self):
    print("playing chess from father")
    
    
class son(father,mother):
  def ride(self):
    print("riding bicycle")

o=son()
o.ride()
o.chess()
o.chess()