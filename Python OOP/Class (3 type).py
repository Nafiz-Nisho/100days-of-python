# Type 1 - instance mathod *

# What I DO?
# I want to create a class/template for each PC "NAME" or "MODEL" number in general.

class My_Pc:
  # creating Constructor  (Constructor in python is a special method that is called when an object is created)
  def __init__(self, NAME, MODEL): 
    self.Pc_Name = NAME
    self.Pc_Model = MODEL

  #  creating instance mathod (In the Python programming language, an instance of a class is also called an object.)
  def details(self):
    print(" PC Name is:", self.Pc_Name, "PC Model is", self.Pc_Model)
# template or blue print is ready.......................................................................


# object is create
Pc_1 = My_Pc("LENOVO", 2023)
Pc_2 = My_Pc("Dell", 2024)


# call in object
Pc_1.details()
# OUTPUT:  PC Name is: LENOVO PC Model is 2023
Pc_2.details()
# OUTPUT: PC Name is: Dell PC Model is 2024

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Type - 2 Class mathod*
class Employe:
  org_name = "Google"
  def __init__(self, name):
    self.name = name
# create class mathod (Decorator)
  @classmethod
  def info(cls):
   return cls.org_name
  
print(Employe.info())
# output "Google" : Now No need extra object create

# Type -3  Static mathod*





