# Basic while loop statement

spam = 0

while spam < 5:
    print("Hello World!!")
    spam += 1
print()

# name = " "
# while name != "Abdul":
#     print("Please enter your name:")
#     name = str(input())
# print("Thank you!!!")
# print()

# Using a break statement in a while loop

# name = " "
# while True:
#     print("Please enter your name:")
#     name = str(input())
#     if name == "Abdul":
#         break
# print("Thank you!!!")

# Using a continue statement in a while loop

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print("spam is " + str(spam))

print("#############################")
#
# password = " "
# while password != "Klopp123":
#     print("Please type password")
#     print("Wrong password please enter again:")
#     password = str(input())
# print("Access granted!!!")

print("#############################")
# Ask the user to input password if the password is wrong 5 times lock the user out.

# password = ""
# count = 0
# print("Please type password")
#
# while password != "Klopp123" and count < 5:
#
#     print("Please retry password again- ")
#     password = str(input())
#     count += 1
#
#     if password == "Klopp":
#         print("Hint: Three numbers are required")
#
#     elif count == 5:
#         print("All five tries are done wait for 1 minute")
#
#     else:
#         print("Hint: LFC current manager")
#
#     if password == "Klopp123":
#         print("Access Granted!!!")
#
#     else:
#         print("Access Denied!!!")

# Example of a for loop
number = 0
for number in range(5):
    print("correct", number)

print()

number = 0
for number in range(1, 5):
    print("correct", number)

print()

number = 0
for number in range(1, 20, 3):
    print("correct", number)

print("#################################")

# write a program that asks user to type his name, after
# 3 times if name is not "Dullah" tell him he has to wait 1 minute
# using a for loop

# For repetition to happen in a for loop use break

print("Start of for loop press 'return or enter' on keyboard")
count = 0
name = " "
for count in range(3):
    print("Enter name again: ")
    name = str(input())

    if name != "Dullah":
        print("Wrong name, try again")

    elif count == 3:
        print("All tries are done, wait one more minute")
        break
    else:
        print("Correct")


# Nested For loops
# For printing coordination
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")
print()

# print out all even numbers from 1 to 10
count = 0
for i in range(1, 10):
    if (i % 2) == 0:
        print(i)
        count += 1
print("We have",count, "even numbers")
