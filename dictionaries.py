# Practicing dictionaries

# Creating a dictionary, empty dictionary
programming_dictionary = {"Bug": "An error ina program that prevents the program from running as expected",
                          "Function": "A piece of code that you can easily call over and over again"}

print(programming_dictionary)
print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

# Looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Clearing out the dictionary
# programming_dictionary = {}
# print(programming_dictionary)
print()
print("Grading Exercise")
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}
# Don't change the code above

# Create an empty dictionary called student_grades.
student_grades = {}

# Write your code below to add the grades to student_grades
for key in student_scores:
    score = student_scores[key]

    if score > 90:
        student_grades[key] = "Outstanding"
    elif score > 80:
        student_grades[key] = "Exceeds Expectations"
    elif score > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

# Don't change the code below
print(student_grades)
