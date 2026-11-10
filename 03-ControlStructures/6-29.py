n = 0
while n < 100:
    if n > 1:
        fir = True
        for i in range(2, n):
            if n % i == 0:
                fir = False
                break
        if fir:
            print(n)
    n += 1
    