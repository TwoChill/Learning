name = ""
age = ""

print("\n\nThe variable 'name' contains: ", name,"<-- This variable is empty\n")
name = input("What the hell is you name?: ")
print("\nNow the variable 'name' contains your name:", name, "\n")

print("\n\nThe variable age contains: ", age,"<-- This variable is empty\n")
age = input("And what is your age?: ")
print("\nNow the variable 'age' contains your age:", age, "\n")

# These two lines show how the use the format in diffrent way's. I prefere the last form on line 10.
print("Hi,",format(name),"! It's nice to meet you. You are ",format(age),"years old.")
print(f"Hi, {name}! It's nice to meet you. You are {age} years old.\n\n")
