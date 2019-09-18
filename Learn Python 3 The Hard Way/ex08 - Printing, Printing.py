# This variable contains 4 empty replacement fields.
formatter = "{} {} {} {}"

# This print function puts the intergers into the replacement field
# and prints them out.
print(formatter.format(1, 2, 3, 4))

# This print function puts the strings into the replacement field
# and prints them out.
print(formatter.format("one", "two", "three", "four"))

# This print function puts the Bollean values into the replacement field
# and prints them out.
print(formatter.format(True, False, False, True))

# This print function puts the variable formatter into the replacement field
# and prints them out. 4 * 4 '{}'.
print(formatter.format(formatter, formatter, formatter, formatter))

# This print function puts the strings into the replacement field
# and prints them out.
print(formatter.format(
    "So we're different colours,",
    "and we're different creeds.",
    "And different people",
    "have different needs."
))
