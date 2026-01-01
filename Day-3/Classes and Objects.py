class Car: # `Class Car`

    model = "SX" # `model` -> Class variable
    # here __init__ is not used, the object is still created but no instance variables are initialized automatically.

car = Car() # `car` -> reference variable, `Car("attributes")` is a Car object

# A `Car` object is created in the memory (heap)
# The reference variable is created `car = Car()`
# The reference variable points to the `Car` object stored in the memory block

print(id(car))

# ---------------------------------------------------------------------------------------------------------------
class Bicycle:
    def __init__(self, name): # self -> references to the current object used, name -> local variable
        self.name = name # instance variable `self.name` is initialised automatically because of __init__

    def intro(self):
        return f"The name of the bicycle is {self.name}"

bike = Bicycle("MTB") # Bicycle("MTB") is a Bicycle object

print(bike.intro()) # python automatically passes the object as self
print(Bicycle.intro(bike)) # here we use class to pass the object to the method manually

# -------------------------------------------------------------------------------------------------------------------

class A:
    x = 10

obj1 = A()
obj2 = A()
obj1.x = 20
print(obj2.x) # 10
# the answer is 10 because when we change the obj1 object's class variable, it is changed in the memory of obj1 not obj2

# --------------------------------------------------------------------------------------------------------------------------

class B:
    var = 5 # shared across all the objects
    def __init__(self, val):
        self.val = val # shared to only object passed at that time

ob1 = B(6)
ob2 = B(7)
print(ob1.val, ob2.val)
print(type(ob1))

# --------------------------------------------------------------------------------

class A:
    def value(self, name):
        self.name = name
        return f"{self.name}"

obj = A()
print(obj.value("Aayush"))
print(obj.value("Piyush")) # data is not saved at once when the object already uses the value method
print(type(obj))

# __init__() is used to initialize data once at object creation, so all other methods can use that data without passing it again.
# Without __init__(), data must be passed each time to methods that need it, or set manually.
# __init__() stores initial data in the object so methods can reuse it without re-passing arguments.

# --------------------------------------------------------------------------------------------------------

class A:
    def __init__(self, name):
        self.name = name

    def value(self):
        return f"{self.name}"

obj = A("Aayush")
print(obj.value())

# With __init__
# Data is initialized once at object creation and reused.

# Without __init__
# Data is initialized each time the method is called and may overwrite previous data.

# ------------------------------------------------------------------------------------------------

# Common built-in classes in Python

# int → integers
# float → decimal numbers
# str → strings
# list → lists
# tuple → tuples
# set → sets
# dict → dictionaries
# bool → True / False
# NoneType → None

# Built-in function-related classes
# function
# range
# enumerate
# zip

# Built-in error classes
# Exception
# ValueError
# TypeError
# IndexError

# Built-in type-related classes
# type
# object (base class of all classes)

# What “everything is an object” means in Python
# Every value in Python is an instance of some class.

# That includes:
# Numbers → objects of int
# Strings → objects of str
# Lists → objects of list
# Functions → objects of function
# Classes → objects of type

# Important consequence

# Because everything is an object:
# Everything has a type
# Everything has attributes and methods
# Everything lives in memory

# ------------------------------------------------------------------------------------------------------------------

# Q. What does type(obj) returns?
# It return the returns the class of the object

x = 10
print(type(x))     # <class 'int'>

a = [1, 2]
print(type(a))     # <class 'list'>

class A: pass
obj = A()
print(type(obj))   # <class '__main__.A'>
