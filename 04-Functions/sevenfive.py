def f(x, y):
    number = int(input("A number : "))
    if number >= x and number <= y:
        return f'Number {number} in the range <{x},{y}>: yes'
    else:
        return f'Number {number} in the range <{x},{y}>: no'