# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# Ok, thats *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This jest takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no arguments
def print_none():
    print("I got notin'.")


print_two("Michael","Leslie")
print_two_again("Michael","Leslie")
print_one("First!")
print_none()
