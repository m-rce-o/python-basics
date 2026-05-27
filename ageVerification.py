age = int(input("What's your age? "))

if age > 18:
    print("You're considered an adult.")
elif 13 >= age <= 18:
    print("You're considered a teen.")
else:
    print("You're considered a child.")