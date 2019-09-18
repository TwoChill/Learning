################################################################################
print("#" * 50)
print(f"\nExersice 20 - Functions Can Return Something - (Practice)\n")
print("#" * 50)
################################################################################

def add(a, b):
    print(f"\nADDING:\t\t{a} + {b} =", (a + b), "\n")
    return a + b

def divide(a, b):
    print(f"DIVIDING:\t{a} / {b} =", (a / b), "\n")
    return a / b

def subtract(a, b):
    print(f"SUBTRACTING:\t{a} - {b} =", (a - b), "\n")
    return a - b

################################################################################

print("\nWhich TWO numbers shall I ADD togehter?")
num1 = int(input("Number 1:> "))
num2 = int(input("Number 2:> "))

print("\nWhich TWO numbers shall I DIVIDE togehter?")
num3 = int(input("Number 1:> "))
num4 = int(input("Number 2:> "))

print("\nWhich TWO numbers shall I SUBTRACT togehter?")
num5 = int(input("Number 1:> "))
num6 = int(input("Number 2:> "))

print("\nAnd finally, what is you lucky number?")
lucky_number = int(input("Lucky Number:> "))

################################################################################

add_ = add(num1, num2)
divide_ = int(divide(num3, num4))
subtract_ = subtract(num5, num6)

print("#" * 50, "\n")
print("Question: \t", (num1 + num2)," + ", (num5 - num6)," / ", (num3 / num4)," - ", lucky_number,"\n")
print("#" * 50, "\n")

# Inside Out! Python works from inside out. INSIDE = Python / OUTSIDE = The Sum or calculation.
new_formula_3 = subtract(-1023, divide(add(add_, subtract_), divide_))

print("#" * 50)
print(f"\nAnswer: {new_formula_3}\n")
print("#" * 50)
################################################################################
