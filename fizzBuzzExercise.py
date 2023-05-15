# Write a program that automatically prints the solution to the FizzBuzz game.
# It should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz"

# When the number is divisible by 5 then instead of printing the number it should print "Buzz"

# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# solution
total = 0
for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 5 == 0:
        print("Buzz")

    elif number % 3 == 0:
        print("Fizz")

    else:
        print(number)

# first trial not correct as the "FizzBuzz" condition is never met. Only the first two are met and all numbers are printed
# total = 0
# for number in range(1, 101):
#
#     print(number)
#
#     if number % 3 == 0:
#         print("Fizz")
#
#     elif number % 5 == 0:
#         print("Buzz")
#
#     elif number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")

