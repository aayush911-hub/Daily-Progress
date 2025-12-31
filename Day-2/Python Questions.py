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
# a = [1, 2]
# b = a
# b = b + [3]
# print(a)

# here 'b' creates a new object
# --------------------------------------------------------------

# a = list((1, 2, 3))
# print(a) # [1, 2, 3] -> Set converted into list

# a = (1, 2, 3)
# b = (4, 5, 6)
# c = list([a,b])
# dif = c[1] # this shows that c is list from outer block but the inner block is tuple only
# print(dif)
# ---------------------------------------------

# a = [[1, 2], [3, 4]] # let [1, 2] -> e, [3, 4] -> f
# b = a.copy()
# b[0] = [9, 9] # here we didn't access the inner objects a[0][0] or a[0][1] or a[1][0] or a[1][1], we just changed the outer container's element [e,f].
# print(a)

# ---------------------------------------------------

def f(a, cache = []):
    cache.append(a)
    return cache

f(4) # [4]
v = f(6) # [4, 6]
print(v) # [4, 6]

def fv(b, cache1 = None):
    if cache1 is None:
        cache1 = []
    cache1.append(b)
    return cache1
fv(5) # [5]
value = fv(8) # [8]
print(value)

