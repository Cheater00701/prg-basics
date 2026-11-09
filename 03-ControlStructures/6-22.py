i = 1
while i <= 30:
    if i % 3 == 0:
        print("THREE")
        if i % 5 == 0:
            print("BINGO")
    elif i % 5 == 0:
        print("FIVE")
    else:
        print(i)
    i += 1