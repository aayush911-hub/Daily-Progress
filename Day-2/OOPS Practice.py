class Car:
    def __init__(self, model, manufacture_year, color, for_sale = True):
        self.model = model
        self.manufacture_year = manufacture_year
        self.color = color
        self.for_sale = for_sale

    def car_model(self):
        return self.model

    def car_year(self):
        return self.manufacture_year

    def car_color(self):
        return self.color

    def car_for_sale(self):
        if self.for_sale:
            return f"{self.model} is for sale"
        else:
            return f"{self.model} is not for sale"

car1 = Car("Mustang", 2025, "Black")
car2 = Car("Corvette", 2026, "Red", False)

# print(f"The model of the car is {car1.car_model()} manufactured in year {car1.car_year()}")
# print(f"{car2.car_for_sale()} but {car1.car_for_sale()}")
# print(f"The color of {car1.car_model()} is {car1.car_color()} and {car2.car_model()}'s color is {car2.car_color()}")

# ---------------------------------------------------------------------------------------------------------------------------------

class Student:
    finished = True
    def __init__(self, name, year, semester):
        self.name = name
        self.year = year
        self.semester = semester

    def sem_finished(self):
        if self.finished: # why self is applied to the global variable in a function
            return f"{self.semester} semester is finished"
        else:
            return f"{self.semester} semester is ongoing"

student1 = Student("Aayush Ojha", "2nd year", "3rd")
# print(f"{student1.sem_finished()}")

# -----------------------------------------------------------------------------------------------

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True
#
#     def eat(self):
#         return f"{self.name} is eating"
#
# class Rabbit(Animal):
#     def type(self):
#         return f"{self.name} is Hervivore"
#
# class Dog(Animal):
#     pass
#
# rabbit = Rabbit("Wind Breaker")
# dog = Dog("Cosmos Destroyer")
# print(rabbit.eat())
# print(rabbit.type())
# print(dog.eat())

# ------------------------------------------------------------------

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def type(self):
        return f"{self.name} is a bird"


class Aquatic:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} can swim")


class LandBird(Bird, Aquatic):
    def __init__(self, name):
        Bird.__init__(self, name)      # Animal → Bird
        Aquatic.__init__(self, name)   # Aquatic

    def fly(self):
        return f"{self.name} can't fly"


bird = LandBird("Penguin")
print(bird.type())
print(bird.fly())
# -----------------------------------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def details(self):
        return f"The name is {self.name}, Roll no. {self.roll_no}"

std = Student("Aayush", 2)
print(std.details()) # The name is Aayush, Roll no. 2
# ------------------------------------------------------------------------

class Per:
    def __init__(self, name):
        self.name = name

class Stu(Per):
    def det(self):
        return f"The name is {self.name}"

st = Stu("Aayush")
print(st.det()) # The name is Aayush

# ---------------------------------------------------------------------------

class Add:
    def ad(self):
        print("A")

class Sub(Add):
    def ad(self):
        print("B")

Add.ad(1)