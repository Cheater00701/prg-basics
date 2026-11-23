def f(a, b):
    x = 0
    y = 1
    s = int()
    zag = int()
    for i in range(0, a):
        s = x + y
        x = y
        y = s
    x = 0
    y = 1
    s2 = int()
    for i in range(0, b):
        s = x + y
        x = y
        y = s2
    return s2 - s
print(f(1,5))