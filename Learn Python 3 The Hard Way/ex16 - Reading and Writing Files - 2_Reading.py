## EXERCISE 16, QUESTION 16.2:

## Write a script similar to the last exercise
## that uses read and argv to read the file you just created.

from sys import argv

script, filename = argv

print(f"""
We're going to read {filename}.
If you don't want to read this file,
press CTRL + C(^C)""")

input("? ")

# Mode 'r' doesn't need to be specified below because it's the default setting.
target = open(filename)

print(f"The {filename} contains the following: \n")
print("#" * 80, "\n")
print(target.read())
print("#" * 80, "\n")

print(f"Now we're closing {filename}!\nGoodbye!")
target.close()
