name = "Abdul"
if name == "Abdul":
    print("Hello Abdul")
    print("Done !!!")
else:
    print("Something is wrong check code")

print()
# if name == "Bob":
#     print("Welcome Bob")
# print("Something is wrong check code")

if name == "Dullah":
    print("Hello Abdul")
    print("Done !!!")
else:
    print("Something is wrong check code")
print()

password = "klopphite"
secret_No = 2000
if password == "klopphite":
    print("Access Granted.")
else:
    print("Access Denied, please try again!!!")

password = "klopphite"
if password == "kloppite":
    print("Access Granted.")
else:
    print("Access Denied, please try again!!!")
print()

if password == "klopphite":
    print("Access Granted.")
elif secret_No > 20:
    print("Welcome Abdul")
else:
    print("Access Denied, please try again!!!")

print()

if password == "klophite":
    print("Access Granted.")
elif secret_No < 2000:
    print("Welcome Abdul")
else:
    print("Access Denied, please try again!!!")

print("#################################################################################################################")
# Ask user for name,age, nationality,field of study, GPA. If age is less than 23 type you are not Abdul, you are input
# if gpa is greater than
print("Hey, welcome to my little code expression/statements")
print("Write down your info below")
print("print name:")
name_ = str(input())
print("print age")
age_ = int(input())
print("print field of study")
field_of_study = str(input())
print("print gpa")
_gpa = float(input())


print("My name is " + name_ + ". I am", age_, "years old. I study "
+ field_of_study + " at the University of Saskatchewan. My GPA is " + str(_gpa) + ".")

if age_ >= 23:
    print("There is a possibility you are Abdul")
elif _gpa > 4.0:
    print("Invalid GPA")
else:
    print("You are not Abdul")


high_income = False
good_credit = True
student = False

# a person can be "Eligible if they have either high income or good credit and they should not be a student

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")


age1 = 22
if 18 <= age1 < 65:
    print("Good")
else:
    print("Wrong")



