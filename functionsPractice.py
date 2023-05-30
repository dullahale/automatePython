# keyword def

# Hurdle 3 exercise answer

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#
#     turn_right()
#     move()
#     turn_right()
#
#     while front_is_clear():
#         move()
#
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()


# Maze solution
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#
#     elif front_is_clear():
#         move()
#
#     else:
#         turn_left()

def greet():
    print("Hello")
    print("Good day")
    print("Welcome")


greet()
print()


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Good day {name}")
    print(f"Welcome {name}")


greet_with_name("Abdul")
print()


# Positional arguments
def greet_with_name_lo(name, location):
    print(f"Hello {name}")
    print(f"Good day {name}")
    print(f"Welcome {name}")
    print(f"How is the weather at {location}")


greet_with_name_lo("Abdul", "Saskatoon")
print()


# Keyword arguments
def greet_with_name_lo(location="Saskatoon", name="Abdul"):
    print(f"Hello {name}")
    print(f"Good day {name}")
    print(f"Welcome {name}")
    print(f"How is the weather at {location}")


greet_with_name_lo()
print()
print("Painting Exercise")


# Write code below this line
def paint_calc(height, width, cover):
    no_of_cans = (height * width) / cover
    rounded = round(no_of_cans)
    print(f"You will need {rounded} cans of paint.")


# Write code above this line

# Don't change the code below
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

print()
print("Prime Number Checker Exercise")

# Write code below this line
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write code above this line

# Don't change any of the code below
n = int(input("Check this number: "))
prime_checker(number=n)
