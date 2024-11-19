# Multilevel inheritance

class Grandfather:
  def ownhouse(self):
    print("Grandpa's house")
    
class father(Grandfather):
  def ownbike(self):
    print("father's bike")

class son(father):
  def ownbook(self):
    print("son have a own book")

o=son()
o.ownbook()
o.ownbike()
o.ownhouse()       
    