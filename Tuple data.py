name = input("Enter your name: ")
age = int(input("Enter your age: "))
occupation = input("Enter your occupation: ")

if age >= 18:
    print(f"{name} is {age} years old and is a {occupation}.")
else:
    print(f"{name} is {age} years old and is not yet an adult.")