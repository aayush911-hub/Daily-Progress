# two variables point to the same object
# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a) # Output: [1, 2, 3, 4]

# two objects have the same value
# a = [1, 2, 3]
# b = [1, 2, 3]
# b.append(4)
# print(a) # Output: [1, 2, 3]

# a = [1, 2]
# b = a
# b += [3]
# print(a) # Output: [1, 2, 3]

# -----------------------------------------------------------
# Important
a = [1, 2]
b = a
b = b + [3]
print(a)

# here 'b' creates a new object
# --------------------------------------------------------------

