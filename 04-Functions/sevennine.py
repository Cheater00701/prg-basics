def f(number, even):
    licz = 0
    if even == True:
        for i in str(number):
            if int(i) % 2 == 0:
                licz = licz + int(i)
        return licz
    elif even == False:
        for i in str(number):
            if int(i) % 2 != 0:
                licz = licz + int(i)
        return licz
