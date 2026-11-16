def f(b):
    def prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    c = 0
    n = 1
    while c < n:
        n += 1
        if prime(n):
            c += 1
    return n