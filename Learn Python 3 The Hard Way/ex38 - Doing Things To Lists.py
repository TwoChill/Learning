# a variable with a string
ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print("Wait there are not 10 things in that list. Let's fix that.")

# .split at ' ' will create a list with the seperate words as items.
stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

# while 6 is not greater then 10.
while len(stuff) != 10:
    # .pop()default deletes last item in a list and returns that item!
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
print("There we go: ", stuff)
print("\nLet's do some things with stuff.\n")
print('stuff[1] =', stuff[1])
print('stuff[-1] =', stuff[-1])
# stuff.pop() == pop(stuff)
print('stuff.pop =', stuff.pop())
print('>>> stuff =', stuff)
# joins ' ' (space) between items in a list, returns string
print('join(stuff) =', ' '.join(stuff))
print('join(stuff) is type =', type(' '.join(stuff)), 'and ONLY returns a string!')
print('stuff =', stuff)
print('\n')
# Places '#' only between items in 'stuff' @ index nr
print('#'.join(stuff[3:5]))
print('stuff =', stuff)
