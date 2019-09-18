name = 'Michael de France'
age = 31 # not a lie

height = 76 # inches
# This line convert Inces to Centimeters.
one_cm = 2.54
height_cm = round(height * one_cm)

weight = 170 # lbs
# This line convert LBS to KG.
one_pound = 2.2046226218487757
weight_kg = round(weight / one_pound)

eyes = 'Brown'
teeth = 'White'
hair = ' Black'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")

# Line added for CM.
print(f"That's {height_cm} in centimeters.")
print(f"He's {weight} pounds heavy.")

# Line added for KG.
print(f"That's {weight_kg} kilograms heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
new_total = age + height_cm + weight_kg
print(f"If I add {age}, {height} inces and {weight} lbs I, get {total}.")
print(f"If i add {age}, {height_cm}cm and {weight_kg}kg, I get {new_total}.")
