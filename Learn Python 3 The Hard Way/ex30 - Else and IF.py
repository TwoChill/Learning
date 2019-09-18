# These are the variables with set values
people = 558
cars = 557
trucks = 8000

# This is the first block with its brancehs.
# This will check to see if the value of variable cars is greater than
# the value of the variable people.
if cars > people:
    print("We should take the car.")
# Only if the above branch evaluates to False, this branch will be evaluated.
elif (cars < trucks) and (trucks > people):
    print("Trucks rule the world!")
# Only if the above branch evaluates to False, this branch will be evaluated.
elif cars < people:
    print("We should not take the car.")
# Only if the above branch evaluates to False, this branch will be evaluated.
else:
    print("We can't decide.")

# This is the second block with its branches.
if trucks > cars:
    print("That's too many trucks!")
elif trucks < cars:
    print("Maybe we could take the tucks.")
else:
    print("We still can't decide.")

# This is the third block with its brancehs.
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's just stay home then.")

# Q.  Try to quess what elif and else are doing.
# 1.    The elif and else are other branches of the same block of code.
#       if the fist branch (if-branch) is False, the second branch will be evaluated.
#       And so on

# Q.   Change the numbners of cars, people, and tucks, and then trace through
#      each if-statments to see what wil be printed.
# 2.    ###

# Q.   Try some more complex boolean expression like car> people or truck < cars.
# 3.    ###

# Q.   Above each line write a English descriptiojn of what the line does.
# 4.    ###
