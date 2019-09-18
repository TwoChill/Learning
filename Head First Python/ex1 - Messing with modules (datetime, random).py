from datetime import datetime
from os import sys

import time     # use dir(time) in IDLE to querey a object.
import random   # use dir(random) in IDLE to querey a object.
# Import custom module
import getcwd


# Displays current version of Python
print(sys.version)

# Displays current working directory.
print('\nYou are here -->:', getcwd.where_am_i())

# Displays current time
print('\n\nCurrent time:', time.strftime("%H:%M"))

# Creates a radom number between 1 - 60
randomnr = random.randint(1, 60)

# Creates a list from 1 - 59 with interfall of 2
odds = [o for o in range(1, 60, 2)]

# Sets the current year to a var as a int.
# right_now = datetime.today().year

# Sets the current month to a var as a int.
# right_now = datetime.today().month

# Sets the current day to a var as a int.
# right_now = datetime.today().day

# Sets the current hour to a var as a int.
# right_now = datetime.today().hour

# Sets the current minute to a var as a int.

print(f"\n## We're waiting {randomnr} seconds between each iterations! ##")


for i in range(5):
    right_now = datetime.today().minute

    if right_now in odds:
        print("\nThis minute seems a little odd..")
    else:
        print("\nNot a odd minute..")
    
    time.sleep(randomnr)

