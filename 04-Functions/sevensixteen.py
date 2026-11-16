def f(n):
    num1 = 1
    num2 = 0
    num3 = 0
    for i in range(n - 2):
        num3 = num2
        num2 = num1
        num1 = num2 + num3
    return num1