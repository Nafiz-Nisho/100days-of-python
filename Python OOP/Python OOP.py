
# Class

# what is class? 

# EXPLAIN : 
# class in Python is a blueprint for creating objects, 
# encapsulating data for the object, and methods to manipulate the data.
# "class as a recipe for creating objects"

# Python None-Paramiterized constructor()
class Employee:
   # Mathod
   def __init__(self):
      print("Emloyee is created")

Employee_1 = Employee()
Employee_2 = Employee()

# output : 
# Emloyee is created
# Emloyee is created


# Python Paramiterized constructor()
class Employee:
      # Mathod
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return self.name, self.age 

# Creating an object (instance) of the class
person1 = Employee("Nafiz", 19)

# Accessing attributes and calling methods of the object
print(person1.info())
# output: ('Nafiz', 19)

# use object rendom
print(person1.name)
# output : nafiz

# So Class is Employee >>>> Employee is created object >>> preson1 is object.

  