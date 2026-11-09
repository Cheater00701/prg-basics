age = int(input("Enter your age :"))
if age < 13 and age >= 0:
    print("You are just a child")
elif age <= 19:
    print("You are a teen")
elif age <= 64:
    print("You are an adult")
elif age > 65:
    print("You are a senior")
else:
    print("Error; Invalid number")