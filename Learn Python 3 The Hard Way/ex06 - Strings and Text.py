# Variable with 10 as a value
type_of_people = 10

# Another Variable with a f-string as it's value. In it are replacement fields.
x = f"There are {type_of_people} types of people."

# Variables with a string as its value.
binary = "binary"
do_not = "don't"

# Another Variable with a f-string as it's value. In it are replacement fields.
y = f"Those who know {binary} and thos who {do_not}."

# The print function that prints out variable x and y
# which are strings with replacement fields in them.
print(x)
print(y)

# Print function that prints out a f-string
# with the variable x and y in its replacement field.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# A variable with Flase  Boolean value as its value.
# And another variable with a normal string as its value plus
# an empty replacement field behind it.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# This print function has the previous value passed into it with
# the format methode which in its self has a variable passed through it.
# This will allow the empty replacement field to be automaticly filled in.
print(joke_evaluation.format(hilarious))

# Variables with a string as its value.
w = "This is the left side of..."
e = "a string with a right side."

# This print function prints out one string which has been concatenated together.
# It is possible to concatenat two or more strings together because they are
# of the same datatype.
print(w + e)
