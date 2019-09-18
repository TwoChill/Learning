people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The word is doomed!")

if people > cats:
    print("Not many cats! The word is saved!")

if people < dogs:
    print("The word is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= people:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
#print("People are dogs.")
    print("People are dogs.")

# Exercise 29
# Q.    WHAT DO YOU THINK THE IF DOES TO THE CODE UNDER IT?
# 1.    The if-statments checks to see if a condition is True or False.
#       If it's True, it'll run that Boolean expression on that branch.
#       otherwise, it will skip it.

# Q.    WHY DOES THE CODE UNDER THE IF NEED TO BE INDENTED FOUR SPACES?
# 2.    The indent needs to happen because otherwise Python doesn't know what code
#       to run. Also it's a good style stated in the PEP8 guidlines.
#       Your code also reads better.

# Q.    WHAT HAPPENS IF IT ISN'T INDENTED?
# 3.    Otherwise you'll get a IndentationError.

# Q.    CAN YOU PUT OTHER BOOLEAN EXPRESSIONS FROM EXERCISE 27 IN THE IF-STATMENT?
# 4.    Yes you can. Infact, that is what I've done to make a 'exam-progam' for myself.

# Q.    WHAT HAPPENS IF YOU CHANGE THE INITAL VALUES FOR PEOPLE, CATS, AND DOGS?
# 5.    Depending on the changes made, the answers given by the if-statments will differ.
