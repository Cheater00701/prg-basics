def f(x, y):
    suma = 0
    for i in range(x, y):
        if i % 2 == 0  and i < 0:
            suma = suma + 1
    return suma