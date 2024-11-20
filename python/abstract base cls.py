from abc import ABC, abstractmethod

class Bank(ABC):
  @abstractmethod
  def loan(Self): pass
  
  @abstractmethod
  def credit(Self): pass
  
  @abstractmethod
  def debit(Self): pass
  
class HDFC(Bank):
  def loan(Self):
    print("we can provide 7.5% Interest loan")
    
  def credit(Self):
    print("HDFC provide credit")
    
  def debit(Self):
    print("HDFC provide debit")
    
  def card(self):
    print("we can provide card")
  
  
o=HDFC()
o.loan()
o.credit()
o.debit()
o.card()

  