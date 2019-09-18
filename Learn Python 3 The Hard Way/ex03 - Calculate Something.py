# Salary check. I got carried away a bit.
# This was not excercise but I wanted to know if I still rememberd thinks I learn a while back.

## Catch errors with Try and Except!
## use lstrip on line 20

name = str(input("\nHi! My name is Salary Checker. \nWhat is your name?: "))
print("\nHi, " + name + ", It's good to meet you!\nNow lets begin!!\n\n")

months = int(input("Over how many MONTHS do you want to calculate your salary?: "))
print("Oke, I will put in " + str(months) + " month(s).\n")

days = int(input("Now tell me " + name + ", how many DAYS did or do you work in 1 week?: "))
print("Allright, I'll tell the calculator that you've worked " + str(days) + " days in 1 weeks.\n")

hours = int(input("And how many HOURS did or do you work on average in 1 day?: "))
print(str(hours) + " hours per day huh?.... That's", ((hours * 4) * 4), "hours in 1 week! Good job!!!\n")

money = float(input("Last question, I promise!\nHow much did or do you get paid PER HOUR?: "))


print("\n\n\nYour salary, on average, over " + str(months) + " month(s) is: €", float((((hours * 4) * 4) * months) * money), ",-!\n\n\n")

print("The End\n\nRestart this program again for another Salary Calculation!\n\n")
