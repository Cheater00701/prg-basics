discount = float(0.25)
product = 40
exp_val = 1 - discount
amount = 5
final = 0
for i in range(amount):
    if final > product:
        final += product
    else:
        final += product * exp_val
print(f"Product price ${product}")
print(f"Amount of products purchased: {amount} pcs")
print(f"Amount to pay: ${final}")
