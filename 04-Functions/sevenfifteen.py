def f(detector):
    people = 0
    for n in detector:
        if n == '+':
            people += 1
            if people == 3:
                return True
        elif n == '-':
            people -= 1
    return False