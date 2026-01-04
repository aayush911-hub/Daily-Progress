Date: 29/12/2025

### Learning Python Concepts

---
Q. Difference between return and print()
   - return -> Gives value back to the function call.
      ``` python
        def f():
            return 10
    
        y = f()
        print(y)
      ```
        Output:

      ``` python
      10
      ```
  
   - print() -> Prints the value written in it.
      ``` python
      print("Hello World!")
      ```
      Output:
      ``` python
      Hello World!
      ```
---
Q. Datatype of 
   ``` python
   result  = None
   ``` 
_Answer_: 

None represents “no value / absence of value” in Python and has its own type called **_"NoneType"_**.

---
Q. Why Python allows functions to be defined after they are used?

_Answer_: 

The python reads the entire file first from the starting to the end. 

While reading the file python keeps the function definition in its mind and when the function call is made the function definition saved in the memory is accessed.

If the function definition is not before the function call then:

- Then the function will be called.
- There will be no saved function definition in the memory.
- Which will result into error.

---

Q. Write a code for returning the area and circumference of the circle.

_Answer_:

``` python
import math as m
def value(radius):
    return m.pi*(radius**2), 2*m.pi*radius
   
area, circumference = value(6)
print("Area:", area)
print("Circumference:", circumference)
```
_Output_:
``` python
Area: 113.09733552923255658465516179806
Circumference: 37.699111843077518861551720599354
```

---

Q. What is a Module?

_Answer_:

Module is a python file that contains the reusable code like variables, functions and classes.

---

Q. Why is this preferred?
``` python 
import math
```
over
``` python 
from math import *
```
_Answer_:

``` python 
import math
```
- It is preferred because it prevents overwriting over the variables/functions.

- It also prevents the _Namespace Pollution_.

    - Namespace is like a folder that groups the related identifiers (variables, functions, classes) to prevent the naming conflicts.
    - Namespace Pollution is a problem in which too many names are introduced into the shared namespace.

---

Q. What happens if two modules contain a function named area() and both are imported using * ?

_Answer_:

The last imported module will overwrite the previous module which will create unexpected results.

---

Q. Can you modify `python_4a.pi` from another file? If yes, should you?

_Answer_:
``` python
python_4a.pi = 10
```
yes, we can modify it. But we should not modify it because it can cause unexpected outcomes across the files.

---

Q. What is the value of `__name__`:
- when a file is run directly?
- when imported?

_Answer:_

- When a file is running directly the value is 
    
  ``` python
  __name__ = "__main__"
  ```
- When a file is not running directly the value is
  ``` python
  __name__ = "filename"
  ```

---

Q. What happens if the `main()` function is called outside the `__name__` block ?

_Answer:_

The `main()` function will be accessed when the file is not running directly.

---

Q. What will happen here?
``` python
x = 10

def func():
    x = 5

func()
print(x)
```
_Answer:_

The Output will be:
``` python
10
```
because here:
``` python
x = 10 # is a Global Variable

def func():
    x = 5 # is a Local Variable

func()
print(x)
```
As `x = 5` is Local Variable, it doesn't change the global value of `x`.

---
Q. How can you change a Global Variable? Explain with an example. 

_Answer:_
``` python
x = 10 # is a Global Variable

def func():
    global x
    x = 5 # is a Local Variable

func()
print(x)
```
Output:
``` python
5
```
---

Q. Why is it a bad idea to modify globals?

_Answer:_

- Makes code hard to debug
- Causes unexpected side effects
- Breaks modularity and reusability

---

Q. Why should input() almost never be inside utility modules?

_Answer:_

Utility modules should:
- Only process data.
- Not depend on user interaction.
- It makes code reusable, testable, and import-safe.
---

Q. What breaks if two files import each other?

_Answer:_

Two files importing each other cause:
- Partially loaded modules.
- AttributeError or unexpected behavior.
- Python cannot finish loading either module properly.
---

Q. Predict the output:
``` python
def f(x=[]):
    x.append(1)
    return x

print(f())
print(f())
```
_Answer:_

``` python
[1]
[1, 1]
```
---

Q. Why is the upper code dangerous?

_Answer:_ *Search the answer tomorrow*

---

Q. What is the difference between a list, set and a tuple?

_Answer:_

- List:

    - Represented by `[]`.
    - Duplication is possible.
    - Mutable (Changing the elements after the declaration of the variable).
  

- Set:

    - Represented by `{}`.
    - Duplication is not possible.
    - Immutable (Elements can't be changed after the declaration of the variable).


- Tuple:

    - Represented by `()`.
    - Duplication is possible.
    - Immutable.
  
---

Q. What happens when we try to change the elements in tuples?

_Answer:_

It will raise `TypeError` statement.

- `TypeError` statement is used when we try to apply the operation on the unsupported data type.
    
  - For example: When try to change the immutable object like a Tuple.

---

Q. What is the output:
``` python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```
_Answer:_

Output: 
``` python
[1, 2, 3, 4]
```
Working:

- `a = [1, 2, 3]` -> 'a' is storing the reference value of the list.


- `b = a` -> The reference value which was stored by 'a' is passed to 'b'.


- `b.append(4)` -> The reference stored in 'b' is accessed which refers towards 'a' which refers towards the list. So, directly in the list the value '4' is appended at the end of the list.


- `print(a)` -> gives the result `[1, 2, 3, 4]`

---

Q. Difference between:
``` python
a = [1, 2, 3]

b = a
# and
b = a.copy()
```
_Answer:_

- `b = a` saves the reference point towards the list.
- `b = a.copy()` copies the list into 'b' , i.e: creates a new list.

---

Q. What does slicing in list return — a reference or a copy?

_Answer:_

Slicing creates the `shallow copy`.

The slicing returns the copy in case of `1-Dimensional` list.

- `a[:]`creates a new list object.

- The elements are copied into the new list.

- `b` points to this new list, not `a`
    ``` css
    a ─> [1, 2, 3]
    b ─> [1, 2, 3]   (different object)
    ```

In case of `2-Dimensional` list the outer list is copied but inner lists still share reference.

- Shallow copies the container not the nested objects inside it.
    
    - `Shallow Copy`: A shallow copy creates a new container, but the elements inside still reference the same objects as the original.
      - Outer list → new
      - Inner objects → shared
        ``` css
        if a = [[1,2], [3,4]]
        
        Outer list -> [[1,2], [3,4]]
        └── Inner list [1, 2]
        └── Inner list [3, 4]
        ```

If we want changes in one list and NEVER affect other one, then we do deep copy:
``` python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 99
print(a)  # [[1, 2], [3, 4]]

```
- `deepcopy()`: A deep copy creates:

    - A new outer container.

    - New copies of all nested objects.
    
    - So no data is shared between the original and the copy.

--- 

Q. Predict the Output:
``` python
x = [1, 2, 3]
y = x[:]
y[0] = 10
print(x)
```
_Answer:_

Output:
``` python
[1, 2, 3]
```
---

Q. Predict the Output:
``` python
a = [[1, 2], [3, 4]]
b = a[:]
b[0][0] = 99
print(a)
```
_Answer:_

Output:
``` python
[[99, 2], [3, 4]]
```
---

Q. Predict the Output:
``` python
s = {1, 2, 2, 3}
print(s)
```
_Answer:_

Output:
``` python
{1, 2, 3}
```
---

Q. What is a dictionary key?

_Answer:_ 

A dictionary key is a `unique`, `immutable` identifier used to access a value in a dictionary.

---

Q. What happens if two dictionary keys are the same?

_Answer:_ 

The recently written dictionary key overwrites the previous value.

---

Q. Does dictionary also use referencing ?

_Answer:_

- A dictionary variable stores a reference to the dictionary object.

- Values inside the dictionary can also be references.

``` python
d1 = {"a": [1, 2]}
d2 = d1

d2["a"].append(3)
print(d1)
```

Output:
``` python
{'a': [1, 2, 3]}
```
---

Q. Dictionary can be sliced or not ?

_Answer:_

No, the Dictionary can't be sliced.

But we can shallow copy the dictionary.

``` python
d2 = d1.copy()
```
- Creates a shallow copy of the dictionary.

- Keys and values are copied by reference.

Example:
``` python
d1 = {"a": [1, 2]}
d2 = d1.copy()

d2["a"].append(3)
print(d1)
```

Output:
``` python
{'a': [1, 2, 3]}
```
---

Q. What is the difference between:
``` python
d.get("x")
d["x"]
```
_Answer:_

- `d.get("x")` -> gives the value at the key `x`. If the key doesn't exist it returns `None`.
- `d["x"]` -> gives the access to the key `x`. If the key doesn't exist it returns `KeyError`.

---

Q. Predict Output:
``` python 
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)
print(a | b)
print(a and b)
print(a or b)
```
_Answer:_

Output:
``` python
{3}
{1, 2, 3}
{3, 4, 5}
{1, 2, 3}
```
- `&` means the `intersection` between the elements.


- `|` means the `Union` of the elements.


- `and` uses the boolean logic to return the result. `A` is non-empty that's why it's `True`.

  - If `A` is False → `return A`

  - If `A` is True → `return B`


- `or` uses the boolean logic to return the result. 

  - If `A` is False → `return B`

  - If `A` is True → `return A`

---

Q. Why sets are unordered ?

_Answer:_

Sets are unordered because they are implemented using hashing, not indexing.

---

Q. What is Hashing ?

_Answer:_

Hashing is the process of converting data into a fixed-size `hash value` (number) using a hash function.

- Each set/dictionary element gets a hash value

- Python uses this hash to store and quickly find elements

Due to Hashing:

- Very fast lookup

- Ensures unique placement of elements

Example:
``` python
hash("apple")
hash(10)
```
---

Q. What is Hash Value ?

_Answer:_

A hash value is a fixed integer number produced by a hash function from some data. Used to store and locate data quickly in sets and dictionaries.

``` python
hash(10)
hash("apple")
```
Key properties:

- Same object → same hash (within a run)

- Different objects → usually different hashes

- Immutable objects have hash values

- Mutable objects do not

---

Q. Sets are mutable so why hash values are assigned ?

_Answer:_

Sets are mutable so hash values are not assigned to the sets but the objects inside the set are hashable because the objects in the set are Immutable.
``` python
{1, 2, 3}          # valid ( 1, 2, 3 -> are immutable)
{[1, 2], [3, 4]}  # error (lists are unhashable)
```
---

Q. When should you use `defaultdict` ?

_Answer:_

You should use `defaultdict` when you want a dictionary to automatically create a default value for missing keys.

Example:
``` python
from collections import defaultdict

d = defaultdict(int)
d["a"] += 1
print(d)
```

Output:
``` python
{'a': 1}
```

**Important:** 
Use `defaultdict` when keys may not exist yet.

---

Q. Show an example in which one dictionary contains another dictionary.

_Answer:_

``` python
val = {"a": 1, "b": 2, "c": 3}

res = {"d": 4, "e": 5, "d": val}

print(res["d"])
```

Output:
``` python
{'a': 1, 'b': 2, 'c': 3}
```
**Important:** 

- `{x}` → set

- `{"key": x}` → dictionary

- Dictionaries cannot be elements of sets

- Dictionaries can be values inside dictionaries
---

Q.

_Answer:_

