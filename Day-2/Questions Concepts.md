Q. Why does this change `a`, but the integer example does not?
``` python
a = [1, 2]
b = a
b += [3]
```
_Answer:_

In this example `+=` performs mutation on `b`. That's why the elements do not change.

Q. What will be the output?
``` python
a = [1, 2]
b = a
b = b + [3]
print(a)
```
_Answer:_

In this example `+` performs addition on `b`. 

Because of which a new object is created for `b`.

Output:
``` python
[1, 2, 3]
```
