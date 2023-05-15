# Password Generator Project
# This a program that generates password for a user based on the letters, numbers and symbols given
# This program asks the user how many letters, numbers and symbols they want in the password and generates
# a random password in that order e.g letter-numbers-symbols
# there are two ways of solving this program the easy mode and hard mode
# The first method i used to solve this was using three different for loops.

import random as rand
import secrets as sec

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Solution 1
# the solution here print sets of letters first followed by set of numbers then set of symbols

password = ""
for i in range(1, num_letters + 1):
    random_letters = rand.choice(letters)
    password = password + random_letters

for i in range(1, num_numbers + 1):
    random_numbers = rand.choice(numbers)
    password = password + random_numbers

for i in range(1, num_symbols + 1):
    random_symbols = rand.choice(symbols)
    password = password + random_symbols

print(password)


# Solution 2
# use a list instead of a string
# used same for loop format as the solution 1
# created a new string called password2_shuffled were i used the rand.sample method to shuffle the elements in the list
# used .join to turn the elements in the list into string

password2 = list()
for i in range(1, num_letters + 1):
    random_letters = rand.choice(letters)
    password2.append(random_letters)

for i in range(1, num_numbers + 1):
    random_numbers = rand.choice(numbers)
    password2.append(random_numbers)

for i in range(1, num_symbols + 1):
    random_symbols = rand.choice(symbols)
    password2.append(random_symbols)

password2_shuffled = rand.sample(password2, len(password2))
mixed = "".join(password2_shuffled)

print(mixed)

