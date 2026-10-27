###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
print("#2 second program:")
speed_kmh = 70
speed_ms = speed_kmh / 1000 * 60
print(speed_kmh, "km/h = ", speed_ms, "m/s")
print("#1 first program:")
###
# A program for swapping two varable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

# swap the values
e = x
x = y
y = e

print("After swapping: x=", x, "y=", y)
print("program that calculates the length of the diagonal of a rectangle :")
###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
print(diagonal)
print("#6 A Program that calculates distance of the horizon")
h = float(input("Enter height in meters: "))
d = 3.57 * math.sqrt(h)
print(f"The distance you see in kilometers is: {d}")
window= 3.57 * math.sqrt(20)

print(f"The distance you from the window is: {window}")

print("#7 A program that calculates and prints")
###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8000000000
north = 7200000000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)
print("Southern Hemisphere: ", south)
print("Southern Hemisphere in %: ", south/total*100)
###
# A program that calculates and prints
# the average grade of a student
#
math = 5
art = 4
music = 5
history = 3
average = math + art - music + history / 4
print(f"Average grade is, {average}")


###
# Printing student's personal data
#
name = "Adam"
year = 16
futureyear = year + 6
heit = 205
print(f"My name is {name}.I am {year} years old, and my height is {heit} cm. In 6 years I will be {futureyear} years old. ")
###
# Write a program that calculates and prints
# the income of a family per person. To print the results
# in a readable form, use f-strings.
#
father_income = 5450
mother_income = 4920
family_members = 5
total_income = father_income + mother_income
income_per_person = total_income / family_members
print(f'Total family income is {total_income}, and income per person is {income_per_person}')
