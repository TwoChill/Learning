def add(a, b):
    print(f"ADDING \t\t{a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING \t{a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING \t{a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING \t{a} / {b}")
    return a / b

print("\nLet's do some math with just functions!\n")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"\nAge: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("\n\nHere is a puzzle:\n")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("\nThat becomes: ", what, "\n")
print("#" * 50, "\n\nCan you do it by hand? \t\tEXERCISE 21.2\n")
print("#" * 50)

print('''
iq = 50
Divide \t\t= \t(iq / 2) \t= 25

weight = 180
Multiply \t= \t(180 * Divide) \t= 4500

height = 74
Subtract \t= \t(74 - Multiply) = -4426

age = 35
Add \t\t= \t(35 + Subtract) = -4391
''')
