# Decorators : Functions that modifies the other functions without changing their source code

# ----------------------------------------------------------------------------------------------------

def add(a,b):
    return a+b

class Value:
    def __init__(self, c, addition):
        self.c = c
        self.addition = addition

    def sub(self):
        return self.addition - self.c

obj = Value(4, add(5, 6))
# print(obj.sub())
value1 = obj.sub
print(value1()) # internally value1() is Value.sub(obj)

# ------------------------------------------------------------------------------

######             TRICKY(topic)                 #####

def hello():
    print("Hi")

value = hello
print(value())
# so in this code hello -> function object
#                                 |
#                                 |-> print("Hi")
# now because value = hello so,
# value -> hello -> function object
#                           |
#                           |-> print("Hi")
# now when we do value() it invokes hello() function and ultimately prints "Hi"
# ----------------------------------------------------------------------------------------------------

# Higher Order Function :- takes the function as argument or returns a function
# Decorators are called as higher order functions because they take functions as input and give the modified functions as output

def name(first_name, last_name):
    return f"{first_name} {last_name}"

def study(branch, full_name):
    return f"{full_name} studies in {branch}"

info = study("CSD", name("Aayush", "Ojha"))
print(info)




