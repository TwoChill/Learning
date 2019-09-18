print("#" * 10)
print("WHILE LOOP")
print("#" * 10)
print("\n")

seperator = "-"
i = 0
numbers = []

while i < 6:

    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now ", numbers)
    print(f"At the bottom i is {i}")
        # 13 is the extra num char of line 16
    print(seperator * (len(str(numbers)) + 13))

print("\nThe numbers: ")

for num in numbers:
    print(num)

print("\n")
print("#" * 36)
print("CODE CHANGE: WHILE LOOP + INCREMENT")
print("#" * 36)

# Q1.   Convert this while-loop to a function that you can call,
#       and replace 6 in the test (i < 6) with a variable.

# Q2.   Add another variable to the function arguments that you van pass in
#       that lets you change the +1 on line 36 so you can change how much it
#       increments by.


def while_num(num, increment):
    i = 0
    numbers = []

    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment                          # <- 1 += 6
        print("Numbers now ", numbers)
        print(f"At the bottom i is {i}\n")
        print("Incremented by ", increment, )
        print(seperator * (len(str(numbers)) + 13), "\n\n")


    print("The numbers: ")

    for num in numbers:
        print(num)


num = int(input("\nWhat kind of number are you thinking about? :> "))
increment = int(input("\nHow much do you want to increment? :> "))

while_num(num, increment)


print("\n")
print("#" * 36)
print("CODE CHANGE: FOR LOOP + INCREMENT")
print("#" * 36)


# Q3.   Write it to use for -loops and range.
#       Do you need the incrementor in the middle anymore?
#       What happens if you de not get rid of it?

num = int(input("\nWhat kind of number are you thinking about now? :> "))
increment = int(input("\nHow much do you want to increment? :> "))
n = 0
number = []

for n in range(0, num, increment):
    print(f"At the top i is {n}")
    number.append(n)

    n += increment
    print("Numbers now ", number)
    print(f"At the bottom i is {i}\n")
    print("Incremented by ", increment, )
    print(seperator * (len(str(number)) + 13), "\n\n")

print("The numbers: ")
for num in number:
    print(num)
