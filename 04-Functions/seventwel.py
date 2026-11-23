def f(n):
    base = str()
    for i in range(1, n + 1):
        if i == n:
            base = base + '*'
            return base
        base = base + '*/'
    return base