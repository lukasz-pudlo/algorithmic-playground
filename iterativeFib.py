def getFib(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, a + b
    return a


print(getFib(3))

1
a = 1
b = 2

2
a = 2
b = 3

3
a = 3
b = 5
