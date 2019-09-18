# We declare a function named cheese_and_crackers. The function uses two arguments
# named cheese_count and boxes_of_crackers.
# Via the indentation we let Python know what this fucntions function is.
# Which is printing out strings with its arguments in placeholders.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Now we have defined the fucntion; we can use the fucntion to do things for us.

# Here we can pass intertergers to the function.
    # cheese_count will hold the value 20
    # boxes_of_crackers will hold the value 30.
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) # Here we call the function with our own arguments.


print("OR, we can use varibles from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


# Combination of arguments
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
