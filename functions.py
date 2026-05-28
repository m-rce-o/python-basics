def getUserInfo(firstName, lastName, age):
    print(f"Hello, {firstName} {lastName}. You are {age} years old.")

#getUserInfo("Sadie", "Dog", 5)

fName = input("First name: ")
lName = input("Last name: ")
age = input("Age: ")

getUserInfo(fName, lName, age)