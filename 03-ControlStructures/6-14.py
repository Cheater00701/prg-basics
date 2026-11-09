facebook = True
twitter = False
instagram = True
networking = sum([twitter, facebook, instagram])
if networking >= 2:
    print("You are a good influencer!")