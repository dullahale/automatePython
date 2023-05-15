# Write a program that calculates the average student height from a list
# of heights e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

# The average height can be calculated by adding all the heights together and
# dividing by the total number of heights.
# e.g 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights 1146 / 7 = 163.7
# Average height equals 164 to the nearest whole number

count = 0
no_Items = 0
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    # finding the sum of items in a list using for loop
    student_heights[n] = int(student_heights[n])
    count = count + int(student_heights[n])

#     finding the lenght of items in a list using for loop
    no_Items += 1

# average height
average_height = round(count / no_Items)

print(student_heights)
print(count)
print(no_Items)
print(average_height)

# Write a program that calculates the highest score from a List of scores.
# e.g [180, 124, 165, 173, 189, 169, 146]. Do not use max and min functions.

# Print the "The highest score in the class is: x"

student_scores = input("Input a list of student scores ").split()
largest = 0
# problem as it does not cover all the range caus
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if n > largest:
        largest = n

print(student_scores)
print("The highest score in the class is:", largest)

# FOR LOOP for range functions
total = 0
for i in range(1, 101):
    total += i
print(total)

# Write a program that calculates the the sum of all the even numbers from 1 to 100
# including 1 and 100.

total_sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        total_sum += number
print(total_sum)

# OR

total_sum2 = 0
for number in range(2, 101, 2):
    total_sum2 += number
print(total_sum2)
