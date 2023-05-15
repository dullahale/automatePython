# This program says hello and asks for name, age and country of residence.
print("Hello World!!!!")
print()

print("What is your name?")
myName = str(input())
print("My name is " + myName)
print()
# Here the age is registered as a string
print("How old are you?")
age = str(input())
print("I am " + age + " years old")
print()
# Here the age is registered as an int but converted to string because integers can not undergo concatenation only
# strings can
# print("How old are you?")
# age = int(input())
# print("I am " + str(age) + " years old")
# print()

print("How many letters are in your name?")
no_letters = str(len(myName))
print("There are " + no_letters + " letters in my name ")
