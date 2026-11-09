###
# Program that simulates the operation of an electronic thermometer.
#
temperature = float(input("Current temperature input??"))
if temperature >= 35:
    print("It is extermely hot")
elif temperature >= 30:
    print("It is hot")
elif temperature >= 15:
    print("It is pretty warm there")
elif temperature >= 0:
    print("It is cold")
elif temperature < 0:
    print("WARNING!  Be careful. Frosty temperature.")