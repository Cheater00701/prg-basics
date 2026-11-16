def f(amount_to_pay):
    resta = amount_to_pay % 5
    ilosc = amount_to_pay // 5
    resta2 = resta // 2
    ilosc = ilosc + resta2
    resta = resta2 % 2
    ilosc = ilosc + resta
    return ilosc