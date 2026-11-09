fee = float(input("Proszę podać liczbę godzin spedzoną na parkingu: "))
zaplata = 0
if fee > 6:
    zaplata = 20
elif fee <= 6 and fee >= 3:
    zaplata = 15
elif fee <= 3 and fee >= 1:
    zaplata = 5
else:
    print("Nieprawidłowa liczba godzin / Brak zapłaty")
print(f"Dziękuje, do zapłaty: {zaplata} PLN")