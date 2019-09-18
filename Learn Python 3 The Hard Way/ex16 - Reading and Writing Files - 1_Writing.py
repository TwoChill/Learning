                                # the filename argument is: ex16_TextEditorTest.txt
from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit ENTER.")

input("?")

print("Opening file...")
target = open(filename, 'w') # 'w' mode opens the file for writting, truncating the file first'

print("Truncateing the file... Goodbey!")
target.truncate() # In 'w' mode, truncating the file is unnecesary'

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("\nI'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")


## EXERCISE 16. QUESTION 16.3

## There's too much repetition in this file. Use strings, formats, and escapes
## to print out line1, line2 and line3 with just on target.write() command.
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we will close it.\nGoodbye!\n")
target.close()
