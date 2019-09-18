# # From the sys module we import the argv argument variable.
# from sys import argv
#
# # To run this script, you MUST pass THREE command line arguments.
# script, first, second, third = argv
#
# print("The script is called: ", script)
# print("Your first variable is: ", first)
# print("Your second variable is: ", second)
# print("Your third variable is: ", third)


################################################################################


# # In this example we practice with modules and unpacking arguments.

# # To run this script, you MUST pass FIVE arguments in the command line.
# # py '.\ex13 - Parameters, Unpacking, Variables.py' Michael 31yr 193cm 79kg


# This line tells Python that we want to import the argument variable argv.
from sys import argv
# This variable holds the arguments we want to pass to our Python script.
script, name, age, height, weight = argv

print("The name of this script: ", script)

last_name = input('And what is your last name?: ')
print("Your name is: ", name + " " + last_name)

print("Your age is: ", age)
print("Your height is: ", height)
print("Your height is: ", weight)
