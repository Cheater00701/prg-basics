###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    semicenter = (a + b + c) * 0.5
    return semicenter
x = 3
y = 4
z = 5
area = math.sqrt(triangle_area(x, y, z) * (triangle_area(x, y, z) - x) * (triangle_area(x, y, z) - y) * (triangle_area(x, y, z) - z))
print(f'The area of ​​a triangle with sides {x} {y} and {z} is {area}')
x = 5
y = 12
z = 13
area = math.sqrt(triangle_area(x, y, z) * (triangle_area(x, y, z) - x) * (triangle_area(x, y, z) - y) * (triangle_area(x, y, z) - z))
print(f'The area of ​​a triangle with sides {x} {y} and {z} is {area}')

x = 7
y = 24
z = 25
area = math.sqrt(triangle_area(x, y, z) * (triangle_area(x, y, z) - x) * (triangle_area(x, y, z) - y) * (triangle_area(x, y, z) - z))
print(f'The area of ​​a triangle with sides {x} {y} and {z} is {area}')
