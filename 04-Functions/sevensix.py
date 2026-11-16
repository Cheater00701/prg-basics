def hide(card_number):
    ask = str(input("Hide credit car number? "))
    if ask == 'yes':
        censored = card_number[2:12]
        for i in censored:
            i = "*"
        card_number = card_number[0:2] + censored + card_number[12:16]
        return card_number
    return card_number
print(hide('5290312400019022'))