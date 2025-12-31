## OOPS Concepts

----
### Some basic concepts of OOPS

- `Class` - Blueprint for creating Objects.


- `Objects` - Instances for Classes.


- Object Creation - `obj = ClassName()`


- Instance Variable - `self.name = name`


- Calling Methods - `obj.Method()`


- `__init__` - A constructor. Will be called automatically but not automatic if overridden.


- `self` - Refers to the current object. It cannot be used outside the methods.


---
Q. What is Constructor ?

_Answer:_

A constructor is a special method that runs automatically when an object is created.

Initializes the object data -> Set initial state 

Constructor runs once per object.

Example:
``` python
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Aayush")
```
Working:

- Memory Allocated.
- `__init__()` runs automatically.
- `self.name = "Aayush"`

---

### _Inheritance_

``` python
class Child(Parent):
```
- Child class automatically gets:
    
    - Methods
    - Attributes

---

### Method Overriding

- Same method name in parent & child.

- Child version runs first.

Example:
``` python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
```
---

### Super()

`super()` is used when the inheritance is done and want to access the methods and constructors of the Parent class.

`super()` uses `MRO` (Method Resolution Technique) for search order of accessing the methods when overriding.

- Conditions when `super()` is used :-

    1. `Method Overriding`

        Example:
        ``` python
       class Animal:
        def sound(self):
            print("Animal makes a sound")
    
        class Dog(Animal):
            def sound(self):           # overridden method
                super().sound()
                print("Dog barks")
        
        d = Dog()
        d.sound()
        ```
       Output:
        ``` python
       Animal makes a sound
        Dog barks
       ```
       - Without Super
       ``` python
       class Animal:
        def sound(self):
            print("Animal makes a sound")
    
        class Dog(Animal):
            def sound(self):           # overridden method
                print("Dog barks")
        
        d = Dog()
        d.sound()
        ```
       Output:
        ``` python
        Dog barks
       ```
    
    2. `__init__` Overriding
        
       Example:
        ``` python
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
       ```
---


