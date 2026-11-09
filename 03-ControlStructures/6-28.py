prev = 0
fibbo = 1
prev2 = 0
for i in range(20):
    print(fibbo, end=" ")
    prev2 = prev
    prev = fibbo
    fibbo = prev + prev2
    