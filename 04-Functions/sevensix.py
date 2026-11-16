def hide(card_number):
    ask = str(input("Hide credit car number? "))
    if ask == 'yes':
        censored = "*" * 10
        card_number = card_number[0:2] + censored + card_number[12:16]
        return card_number
    return card_number