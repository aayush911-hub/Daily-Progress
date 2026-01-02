class Animals:
    def __new__(cls, *args, **kwargs): # we are creating the new objects manually here
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name

    def sleeping(self):
        return f"{self.name} is sleeping"

rabbit = Animals("Galaxy Destroyer")
# print(rabbit.sleeping()) # Galaxy Destroyer is sleeping
# ------------------------------------------------------------
class Animals:
    # Here when the __new__() is not written then also the object is being created
    # The actual concept between the upper code and this code is that the object is created manually in the upper code -
    # - where no need was of creating the object manually

    def __init__(self, name):
        self.name = name

    def sleeping(self):
        return f"{self.name} is sleeping"

rabbit = Animals("Galaxy Destroyer")
# print(rabbit.sleeping()) # Galaxy Destroyer is sleeping
# ------------------------------------------------------------------------------------------------------------

# How __new__() works for creating an object?
# class A:
#     def __new__(cls):
#         return super().__new__(cls)
#
#     def __init__(self):
#         self.x = 10
#
# obj = A()
#
# what happens here is :-
# 1. super().__new__(cls) passes object.__new__(A)
# 2. a blank object is created in the heap of class A
# 3. __init__() initializes the value x = 10 in the object
# 4. that object reference value is being stored in the reference variable `obj`

# ----------------------------------------------------------------------------------------------------------------

# examples like where the __new__() can be used:

# class Value:
#     def __new__(cls, age):
#         if age < 18:
#             return "No value created"
#         else:
#             return super().__new__(cls)
#
#     def __init__(self, age):
#         self.age = age
#
#     def val(self):
#         return f"congrats in being {self.age} years old"

# ob = Value(18)
# ob1 = Value(17)
# print(ob.val()) # congrats in being 18 years old
# print(ob1) # No value created
# --------------------------------------------------------------------------
class Value:
    def __new__(cls, age):
        if age < 18:
            return 0
        else:
            print("Congrats your value created")
            return super().__new__(cls)


ob = Value(18)
ob1 = Value(17)
# print(ob)
# print(ob1)

# Some examples more copied:

# class Age:
#     def __new__(cls, age):
#         if age < 0:
#             return None      # block creation
#         return super().__new__(cls)
#
#     def __init__(self, age):
#         self.age = age

# a = Age(20)
# print(a.age)   # 20
#
# b = Age(-5)
# print(b)       # None

# ------------------------------------------------

# class PositiveInt(int):
#     def __new__(cls, value):
#         if value < 0:
#             value = 0
#         return super().__new__(cls, value)
# x = PositiveInt(-10)
# y = PositiveInt(5)
#
# print(x)   # 0
# print(y)   # 5

# -------------------------------------------------------------------------------

# obj = 4
# print(obj)
# print(str(obj))
# repr(obj)

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Book(title='{self.title}', pages={self.pages})"

b = Book("Python OOP", 350)

# print(b)
# b
# -----------------------------------------------------------------------------------------------------


class Add:
    def __init__(self, x):
        self.x = x

    # def __add__(self, other, another): # this won't work because __add__() takes only 2 values at a time
    #     return Add(self.x + other.x + another.x)

    def __add__(self, other):
        return Add(self.x + other.x) # return Add(value after the addition)

obj1 = Add(1)
obj2 = Add(2)
obj3 = Add(3)
# obj4 = obj1 + obj2 + obj3 # this fails because the __add__() takes only two values at a time eg: obj1.__add__(obj2) there is no space for 3rd object
temp = obj1 + obj2 # we have to break our process into two parts so that value can come up
obj4 = temp + obj3 # obj4 = Add(6) -> it becomes a vector when return
print(obj4.x)

# key points of __add__()
# 1. __add__() is called automatically by +
# 2. It must take one operand besides self
# 3. It should return a new object
# 4. It allows operator overloading

def __add__(a, c): # As it is outside the class it wil behave as normal method
    return a - c

A = 4
B = 6
D = A+B # here our __ad__() is not used python uses it's built-in __ad__() -> A.__add__(B)
print(D)
# ---------------------------------------------------------------------------------------------------------------------

class Value:
    def __init__(self, x):
        self.x = x

object1 = Value(2)
object2 = Value(2)
print(object1 == object2) # why does object1.__eq__(object2) give the value false? -> because both the objects are different in the memory
                          # the equality operator works as object1 == object2 -> object1 is object2
                          # Without __eq__(), == compares memory identity, not data.

class Equality:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

val1 = Equality(3)
val2 = Equality(3)
print(val1 == val2)

# ------------------------------------------------------------------------------------------------

class Length:
    def __init__(self, lt):
        self.lt = lt

ad = Length([1, 2, 3])
# print(len(ad)) # will give error because len() cannot measure the length of the object

if ad:
    print("The list is not empty") # why this printed when I didn't call __len__()?
else:
    print("The list is empty")

# Reason:
# in -> if obj:
# It checks in this order:
# 1 .Does obj.__bool__() exist?
# 2. Else, does obj.__len__() exist?
# 3. Else → object is considered True by default

# in our example 1st and 2nd conditions both don't exist so the condition automatically picks the default condition (3. option)

class Length1:
    def __init__(self, lt):
        self.lt = lt

    def __len__(self):
        return len(self.lt)

ad1 = Length1([1, 2, 3])
print(len(ad1))

if ad1:
    print("The list is not empty")
else:
    print("The list is empty")

# Hello there