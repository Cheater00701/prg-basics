#def f(number):
#    i = 0
#    k = 0
#    for i in str(number):
#        if str(number).count(str(i)) > 1:
#            k = k + str(number).count(str(i))
#    return k
def f(number):
    number = str(number)
    sum = 0
    for i in number:
        x = number.count(i)
        if x > 1:
            sum += int(i)
    return sum