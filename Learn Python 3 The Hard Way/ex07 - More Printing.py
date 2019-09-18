# These are print statements with one having an empty replacement field which
# has 'snow' passed into it.
print("Mary had a little lamb.")
print("It's fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
# This print statement prints 10x the string character 'dot'.
print("." * 10) # what'd that do?

# Here are 12 variables being declared with diffrent letters as there value,
# to maken the word Cheese Burger printed out on the screen when they are
# concatenated.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# The concatenations happens here. The end of line 26 tells the print statement
# to end with certain character. In this is case its a space. What counts is
# everything between the single-quotes.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
