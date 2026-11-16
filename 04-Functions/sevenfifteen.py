def f(detector):
    people = 0
    for n in range(len(detector)):
        if detector[n] == '+':
            people += 1
        elif detector[n] == '-':
            people -= 1
        if people == 3:
            return True
    return False