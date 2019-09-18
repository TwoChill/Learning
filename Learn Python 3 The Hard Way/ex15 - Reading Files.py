# This line imports the variable argument argv from the sys module.
from sys import argv

# These are the TWO command line arguments you MUST put in when running the script.
script, filename = argv

# This line opens the filename argument and puts it content in a variable.
txt = open(filename)


print("\n\nTHIS IS THE ARGV METHODE TO OPEN A FILE\n")

# This line prints out the name of the filename.
print(f"Here's your file {filename}:\n ")
# This line prints out the txt variable by calling the .read() function.
print(txt.read())

# # This line asked the user to put in the filename again.
# print("Type the filename again: ")
# #This line creates a variable unnoticable to the user.
# file_again = input('>')
#
# # This line uses the previous variable to open the typed in filename
# # and places this in a second variable.
# txt_again = open(file_again)
#
# # This line prints out the second variable which contains the ex15_sample.txt
# print(txt_again.read())
# txt_again.close()


### EX QUESTION ###
# Remove line 18 to 29
# Use only input and try the script that way.

print("\nTHIS IS THE INPUT METHODE TO OPEN A FILE\n")

file_name = input('What is the name of the txt file?: ')
print("\nHere's your filename:", str(file_name), "\n")

txt = open(file_name)   # Here Python makes a "file object"
print(txt.read())       # This is were the file is being read and printed.
txt.close()             # This code closes the file,

# Why is one way of getting the filename better that another?

# Michael: I think the use of the input function instead of the arvg
# is better because it only uses the input from a user.
# The user doesn't start this program from a terminal,
# thus it can't put in the filename before the program runs.

# On the other hand I think the agvr METHODE uses less code and probably uses
# less computing power.
