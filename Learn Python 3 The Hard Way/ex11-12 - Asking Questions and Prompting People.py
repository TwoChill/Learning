# The print function prints a string and the end=' ' argument tells
# the print function to end with a space.

# We also create variables with the inputs from a user. They are stored als values.
print("How old are you?", end=' ')
age = int(input())
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

# Here we print a new sting with the values given from a user.
print(f"\nSo you are {age} years old, you are {height} tall and are {weight} heavy.")


# Here is another way tho use the input() fucntion.
# This line off code uses a variable, input() and the print fucntion in one line.

# name = input('What is you name?', end=' ')    # This creats a TypeError. Input() takes no arguments.
name = input("\nWhat is your name by the way? ")

# This will capitalize all the letters in a variable
name.capitalize()

like_code = input('And do you like to use Python? (Yes/No) ')
future = int(input('What is the number you would think off if I would asked you about the future? '))
future_age = age + future

print(f"\nSo your name is {name}, and your answer to the last question was; {like_code}!")
print(f"\n{name}, you would be {future_age} years old in {future} years!")



# For more on Python --> Go to PyDoc.
# PowerShell - py -m pydoc [...]    # input, open, file, os or sys or whatever.
