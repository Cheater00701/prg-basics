def f(name):
    result = ''
    result = result + name[0]
    count = 0
    for i in name:
        if i == ' ':
            result = result + name[count+1]
        count += 1
    return result
