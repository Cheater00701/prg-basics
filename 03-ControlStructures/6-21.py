plns = int(input("Wprowadź wartość PLNów::"))
piec = plns // 5
dwas = (plns % 5) // 2
jedes = (plns % 5) - dwas * 2
print(f"5 PLN coins:{piec}")
print(f"2 PLN coins:{dwas}")
print(f"1 PLN coins:{jedes}")