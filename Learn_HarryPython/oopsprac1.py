# Create a class programmer for for programmer working in microsoft
class Programmer:
  company ="Microsoft"
  def __init__(self,name,product):
    self.name=name
    self.product=product
  def getInfo(self):
    print(f"The name of the programmer is{self.name} and the product is{self.product}")
  
harry=Programmer("Harry","Skype")
alka=Programmer("Alka","Github")

harry.getInfo()
alka.getInfo()
