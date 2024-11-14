#inheritance & single innheritance in python:

class Nokia:
  company="Nokia India"
  website="www.nokia-india.com"
  
  def contact_details(self):
    print("Address : cherry Road, Nagar Bus stand , salem")
    
class Nokia2922(Nokia):
  def __init__(self):
    self.name="Nokia 1100"
    self.year=1998
    
  def product_details(self):
    print("name      : ",self.name)
    print("year      : ",self.year)
    print("company   : ",self.company)
    print("website   : ",self.website)
    
mobile=Nokia2922()
mobile.product_details()
mobile.contact_details()
          