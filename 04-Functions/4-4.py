###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    wynik = int(str(number)[0]) + int(str(number)[1])
    return wynik

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')