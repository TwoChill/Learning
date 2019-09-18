# Remember, if it says "first," "second," then it's using ORDINAL, so subtract 1.
# If it gives you CARDINAL, like "The animal at 1", then use it directly.

# Check later with Python to see if you were correct.


animal = ['bear','python3.7', 'peacock', 'kangaroo', 'whale', 'platypus']

# Q1.   The animal at 1.                                    <-- CARDINAL
# A.    The animal at 1 is the 2nd animal and is a python3.7..
#       The 2nd animal is at 1 and is a;
#       PYTHON3.7
print("Q1: >>:",animal[1] )



# Q2.   The third (3rd) animal.                             <-- ORDINAL
# A.    The third (3rd) animal is at 2 and is a peacock.
#       The animal at 2 is the 3rd animal and is a;
#       PEACOCK
print("Q2: >>:",animal[(3 -1)] )



# Q3.   The first (1st) animal.                             <-- ORDINAL
# A.    The first (1st) animal is at 0 and is a bear.
#       The animal at 0 is the 1st animal and is a;
#       BEAR
print("Q3: >>:",animal[(1 -1)] )



# Q4.   The animal at 3.                                    <-- CARDINAL
# A.    The animal at 3 is the 4th animal and is a kangaroo.
#       The 4th animal is at 3 and is a;
#       KANGAROO
print("Q4: >>:",animal[3] )



# Q5.   The fifth (5th) animal.                             <-- ORDINAL
# A.    The fifth (5th) animal is at 4 and is a whale.
#       The animal at 4 is the 5th animal and is a;
#       WHALE
print("Q5: >>:",animal[(5 -1)] )



# Q6.   The animal at 2.                                    <-- CARDINAL
# A.    The animal at 2 is the 3rd animal and is a peacock.
#       The 3rd animal is at 2 and is a;
#       PEACOCK
print("Q6: >>:",animal[2] )



# Q7.   The sixth (6th) animal.                             <-- ORDINAL
# A.    The sisth (6th) animal is at 5 and is a platypus.
#       The animal at 5 is the 6th animal and is a;
#       PLATYPUS
print("Q7: >>:",animal[(6 -1)] )



# Q8.   The animal at 4.                                    <-- CARDINAL
# A.    The animal at 4 is the 5th animal and is a whale.
#       The 5th animal is at 4 and is a;
#       WHALE
print("Q8: >>:",animal[4] )
