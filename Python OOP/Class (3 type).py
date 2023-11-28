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

#Explain 2:
# what is do?
# i want compare 2 Cats activity.

class Cat:
  def __init__(self, color, action):
    self.color = color
    self.action = action

  def view(self):
    print(self.color, "cat is", self.action)


  def compare(self, ct):
    if self.action == ct.action:
      print("both cat are jumping")
    else:
      print("They are different")


cat1 = Cat("whit", "jumping")
cat2 = Cat("black", "eating")
cat1.view()
cat2.view()

cat1.compare(cat2)
# OUTPUT : They are defferent
# -------------------------------------------------------------------------------------------------------------------------------------------------

# Encapsulation*
class Studnet:
  # Constructor
  def __init__(self, name, Id):
    self.name = name
    self.__Id = Id
# local instance 
  def info(self):
    print("Name:", self.name , "ID:", self.__Id)

  # private instance
  def set_ID(self, Id):
    if (Id > 0):
      self.__Id
    else:
      print("Ivaild ID, enter id again")
  def get_ID(self):
    return self.__Id 
  # -------------------
  def set_name(self, name):
    self.name = name
  
  def get_name(self):
    return self.name
# ---------------------blue print ready------------

s1 = Studnet("Nafiz", 13123)
s1.set_ID(-477)
# output: Ivaild ID, enter id again
s1.set_name("habib")
# output: Name: habib ID: 13123
s1.info()
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Class or Static variable

# Why need static variable in class or python?

# static variables are used to store data that is shared among all instances of a class. 
# They are declared at the class level and are not tied to a specific instance of the class.

class Player:

  # create static variable 
  team_run = 0
  # ------------

  # Constructor
  def __init__(self, run):
    self.run = run
# -------------------

# creating mathod
  def hit_four(self):
    self.run += 4
    Player.team_run += 4

  def hit_six(self):
    self.run += 6
    Player.team_run +=6
# -----------------------
  
# crating object
shakib = Player(0)
tamim = Player(0)
shakib.hit_four()
tamim.hit_six()
# ---------------
# pint object
print("Shakib :", shakib.run)
# outuput: shakib : 4
print("Tamim : ", tamim.run)
# output: tamim : 6
print("Team run : ", Player.team_run)
# output: Team run : 10
# note : team_run no need create object for call & print, bcz its static variables.


class England:
  
  Eng_Run = 0

  def __init__(self, run):
    self.Eng_run = run 

  def six(self):
    self.Eng_run += 6
    England.Eng_Run += 6

  def four(self):
    self.Eng_run += 4
    England.Eng_Run += 4


Jos_Butler = England(0)
Moen_Ali = England(0)
Jos_Butler.six()
Jos_Butler.six()
Moen_Ali.four()
Moen_Ali.six()
Jos_Butler.six()
print("Jos Butler :", Jos_Butler.Eng_run)
print("Moen ali : ", Moen_Ali.Eng_run)
print("Team Run: ", England.Eng_Run)

# @Property Mathid

# how to use Get and Set value in using @Property mathod for make more smart python code

# make class name
class Product:
# cunstrator 
  def __init__(self, price):
    self.price = price

# use smart way
  @property
  # ---------
# getter
  def price(self):
    return self.__price

  @price.setter
  # price.stter belong property mathod
  
# setter
  def price(self, value):
    # using condition
    if value < 0:
      print("Price cannnot be negitive")
    self.__price = value

# make object
p1 = Product(-50)
# print
print(p1.price)

# OUTPUT : Price cannnot be negitive


# Inheritance
# why use Inheritance? : 
# Ans: actually Inheritance Mathod used for "Don"t Repeat your Code too much"!
# example: 

# Animal_1
# instance class

class Animal_1:
 # Type
  def Fish(self):
    print("Animal 1")
# name
  def name(self):
    print("Octopus")
# porpuse
  def porpose(self):
    print("eating")

# __________________________________
# Animal_2
class Animal_2(Animal_1):
# type
  def Wild_Anima(self):
    print("Animal 2")

# name
  def name(self):
    print("bear")

# porpose

  # def porpose(self):
  #  print("eating")


# ____________________________________
# Animal_3
class Animal_3(Animal_1):
  # type
  def pet(self):
    print("Animal_3")
# name
  def Cat(self):
    print("cat")

# porpose

  # def porpose(self):
  #  print("eating")

# purpose instance method is disabled because every animal has the same purpose.
# Therefore, the inheritance method Animal_1() is used to optimize my code.
# _____________________________________

animal = Animal_3()
animal.porpose()
# OUTPUT : eating

# _________________________________

# The Object in Class **

# issubclass * 

# The issubclass function in Python
#  is used to check if a class is a subclass of another class.
#  In this particular line of code, it checks if the class.

# animal_3 is a subclass of animal_1. If animal_2 is indeed a subclass
# of animal_1, the issubclass function will return True

print(issubclass(Animal_3, Animal_1))
#Output : True
# _______________________________________

# isinstance*
#
# (isinstance(animal, animal_3))

#  is using the Python 
# isinstance function to check if the animal object belongs to the animal_2 class. 
# If it does, the function will return True

print(isinstance(animal, Animal_3))

# Output : True
# ___________________________________________________