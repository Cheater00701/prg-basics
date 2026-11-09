number = int(input("Enter number:"))
i = number
binar = ""
while number > 0:
    rem = number % 2
    binar = str(rem) + binar
    number = number //2
print(binar)