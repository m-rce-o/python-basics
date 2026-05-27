curr_level = int(input("What's the current level? (1-100)"))

if curr_level < 30:
    print("Your gas is at low level. Consider refilling.")
else:
    print("Your gas level is still good.")