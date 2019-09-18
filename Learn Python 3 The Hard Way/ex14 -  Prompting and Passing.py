from sys import argv

script, user_name, pass_word = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f'''
You should never enter you password in a script you don't know, {user_name}!
Because I can hack it .... {pass_word} ... see. ;)''')
print("I'm kiding! Did you like my joke?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have, {user_name}?")
computer = input(prompt)

print(f'''
Alright, so you said "{likes}" about my joke. Thanks for that!
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
''')
