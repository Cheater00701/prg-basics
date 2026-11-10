###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

last = "computer science"[-1]
print('The last character of "computer science" is', last) 

string = "20303"
print(f' Binary string: {str(string)}')
number = 304
binary_number = bin(number)
print(f"Binary representation of number {number} is {binary_number}.")
hex_number = hex(number)
print(f"Hexadecimal representation of number {number} is {hex_number}.")
sign = "€"
sign_rep = ord(sign)
print(f"Integerical representation of {sign} is {sign_rep}")
val = -17
ab_val = abs(val)
print(f"Absolute value of {val} is {ab_val}")