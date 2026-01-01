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

