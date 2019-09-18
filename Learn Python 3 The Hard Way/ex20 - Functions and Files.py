# The argument variable argv is imported from sys(tem) / module.
from sys import argv

# Here we unpack the srgv
script, input_file = argv

# Function 1 with one argument (In this case its 'f' for file)
# It just prints contants of a file as a string.
def print_all(f):
    print(f.read())

# Function 2 with also one argument (In this case its 'f' for file)
# The seek fucntion tells Python from which byte to start from.
def rewind(f):
    f.seek(0)

# Function 3 has 2 arguments. When called upon, it will print the value of
# line_count and the first line of the file in 'f' (or file).
# readline() will remember on which byte it stoped so it can (and does) continue.
# ((The . seek(0) fucntion will move the file to the first byte again))
def print_a_line(line_count, f):
    print(line_count, f.readline())

# New variable with the object open inside.
current_file = open(input_file)


# Function 1 is called and current_file is passed in to it.
# Which has the object of open with the target file dir. It then reads that file.
print("First let's print the whole file:\n")
print_all(current_file)

# Function 2 is called and .seek(0) function is used to begin at the beginning of the file
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

# Function 3 is called to print out al the lines separately.
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
