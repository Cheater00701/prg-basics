cs = input("Are you interested in computer science? (y/n):")
games = input("Do you like playing computer games? (y/n):")
insta = input("Do you have an Instagram account? (y/n):")
academicint = False
comp = False
instagram = False
if cs == "y":
    academicint = True
if insta == "y":
    instagram = True
if games == "y":
    comp = True
print(f"SURVEY RESULTS Interested in computer science: {'Yes' if academicint else 'No'}")
print(f"Playing computer games: {'Yes' if comp else 'No'}")
print(f"Has an Instagram account: {'Yes' if instagram else 'No'}")