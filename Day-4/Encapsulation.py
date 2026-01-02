# what is encapsulation?
# It is the practice of binding the data and methods that operate on the data together, and controlling that how the data should be accessed.

# In simple words:
# Data should not be freely modified
# Interaction should happen through controlled methods

# ------------------------------------------------------------------------------------------------------
# Why encapsulation is needed ?

# Encapsulation helps to:
# 1. Protect data from invalid states
# 2. Hide internal implementation
# 3. Prevent accidental modification
# 4. Enforce rules / validation
# 5. Make code easier to maintain and change
# 6. Without encapsulation → objects become fragile and unsafe.

# ----------------------------------------------------------------------------------------------------------
# There are three types of variables (Public, Protected and Private)

# 1. Public:
# self.age -> Accessible to all, No restriction

# 2. Protected:
# self._age -> for "internal use", Accessible but discouraged

# 3. Private:
# self.__age -> Python renames it internally, Prevents accidental access

# example
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def full_name(self):
#         return f"{self.brand} {self.model}"
#
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
#
# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.brand) # the object is accessible to the user by using the object -> that means the user can set the-
#                       # -value of the object.
# my_tesla.brand = "Mahindra" # the user can change the value of the object
# print(my_tesla.brand)


class Vehicle:
    def __init__(self, brand, model):
        self.__brand = brand # python sees private variable as:- self._Vehicle__brand
        self.model = model

    def get_name(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.brand) # the object is accessible to the user by using the object -> that means the user can set the-
                      # -value of the object.
my_tesla.brand = "Mahindra" # creates a new object named as "brand" is created in which "Mahindra" is the value
print(my_tesla.brand)
print(my_tesla.get_name())

# The variables in object are saved in the form of dictionary
# example:
# {
#   "_Vehicle__brand" : "Tesla", # it is the private variable (original)
#   "brand" : "Mahindra" # it is the new variable created when tried changing brand (new)
# }














