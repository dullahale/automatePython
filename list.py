# Learning lists in python
letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3, 4]
matrix = [[0, 1], [2, 3], [4, 5], [6, 7]]
deci = [1.0, 2.0, 3.0, 4.0]

# You can combine a list of boolean, float, strings, integers together
combined = numbers + letters
print(combined)

long_list = list(range(50))
print(long_list)

chars = list("Hello World!!!")
print(chars)

#printing length of a list
print(len(chars))

# Accessing items in a list
print(letters[0])
print(letters[3])
print(letters[-1])

# Modifying items in a list
letters[0] = "A"
chars[-1] = ""

print(letters)
print(chars)

print(letters[0:3])

print(letters[::-1])

#Unpacking list

new_Numbers = [1, 2, 3, 4, 4, 4, 4, 4, 9]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]
first, *others, last = new_Numbers
print(first, last)
print(others)

#Looping over a list
letters = ["a", "b", "c"]
for i in letters:
    print(i)


# Wanting to get the the index of an item
# enumerate returns a tuple

for i in enumerate(new_Numbers):
    print(i)

# Add/Removing items from a list
new_letters = ["a", "b", "c"]
print(len(new_letters))
# Adding use the append method
new_letters.append("d")
new_letters.append("e")
print(new_letters)
print(len(new_letters))

# Insert to add at a specific position
new_letters.insert(5, "f")
print(new_letters)

# Removing items in a list
new_letters.remove("f")
print(new_letters)

# Removing what is at the end of the list
new_letters.pop()
print(new_letters)

new_letters.pop(1)
print(new_letters)

new_letters.insert(1, "b")
print(new_letters)

# Deleting items in a list
del new_letters[-1]
print(new_letters)

new_letters.append("d")
new_letters.append("d")
new_letters.append("e")
new_letters.append("f")
new_letters.append("g")
print(new_letters)

del new_letters[4:6]
print(new_letters)

# Clearing all objects in a list
# Use the clear

modi_list = list(range(8))
print(modi_list)
modi_list.clear()
print(modi_list)

# Finding index in a list
_inList = list("Hello World")
_inList.index("e")
print(_inList.index("e"))

# To return number of occurrences of item in a list use count
if "l" in _inList:
    print(_inList.count("l"))


# Sorting list use sort ascending order
unorganisedList = [10, 8, 1, 2, 6, 4, 3, 7, 9, 5]
unorganisedList.sort()
print(unorganisedList)

# Sorting list use sort descending order
unorganisedList = [10, 8, 1, 2, 6, 4, 3, 7, 9, 5]
unorganisedList.sort(reverse=True)
print(unorganisedList)

sorted(unorganisedList)
print(unorganisedList)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
items.sort()
print(items)