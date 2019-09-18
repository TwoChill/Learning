from sys import exit

returned = 0

def mayan_temple(returned):
    print("\n\nYou stumbeld upon a ancient Mayan tempel.\n")
    print("In awe you venture inside this beautiful temple.")
    print("At the top you discover a grandiose Mayan alter with a Big Red Shiny Ruby on top.")
    print("Above the alter, written in Mayan hieroglyphs, you read:\n\n'BE AWARE, THIS RUBY IS CURSED!'\n")
    print("Will you _take the ruby_ or do you _leave it alone_?\n")

    choice = input("> ")

    while True:
        if str(choice) == "take the ruby":
            print("\n\nYou take the Ruby and set off a chain reaction inside the temple.")
            print("Everything starts to crumble and you fear for you life.")
            print("You start running away.\n")
            print("While haphazardly dodging imminent death, you got flattend by a gaint Mayan temple stone.")
            dead("\nInstant death.")


        elif str(choice) == "leave it alone":
            print("\n\nYou instantly turn around!\n")
            print("This action made you puke on ancient sacred ground!")
            print("After a few moments you hear the sound of a door opening.")
            print("A second later a strong wind accompanied with a eerie dark voice blows you away!")
            print("The wind and terror of this sound hits your body hard.")
            print("You're getting blown towards a secret door..")
            cthulhu_room(returned)

        else:
            dead("\n\nA tear inside reality opens that kills you six ways to sunday.\nBut only afther you spontaneously combusted, sucking up only your faint ash.")



def gold_room():
    print("\nThis room is full of gold coins.\nHow much do you take?\n")

    try:
        choice = int(input("> "))
    except:
        dead("\n\nThere's glitch in your thinking.. You turn around and still got killed by the bear.")

    if choice < 999:
        print("\nNice, you're not greedy! You win!!")
        print("As a reward you'll get a Big Red Shiny Ruby!!\n")
        exit(0)
    else:
        dead("\nYou greedy bastard!")


def bear_room():
    print("\nThere is a bear here.\n")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print('\nYou\'re contemplating:\nShould I _taunt_ the bear or should I _take his honey_?"\n')
    print("How are you going to _move_ the bear?\n")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take his honey":
            dead("\nThe bear looks at you then slaps you face off.\nYou're dead!")
        elif choice == "taunt bear" and not(bear_moved):
            print("\nYour taunt worked! The bear has moved from the door.")
            print("You can go through it now.\n")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            print("\nYour taunt failed!\n")
            dead("It charged and chews your legs off.")
        elif choice == "move bear" and (bear_moved):
            dead("\nThe bear between you and the door just bit you in half.. (-_-)")
        elif choice == "move bear" and not(bear_moved):
            print("\nSomehow, this bear is to lazy to attack and let itself be move.")
            print("You can go through it now.\n")
            bear_moved = True
        elif choice == "open door" and bear_moved:
            gold_room()
        elif choice == "open door" and not(bear_moved):
            dead("\nThe bear between you and the door just bit you in half.. (-_-)")
        else:
            if choice == "taunt":
                print("\nTaunt _what_? The bear? Me?? A Mayan God???\n")
            elif choice == "move":
                print("\nMove _what_? Yourself? The bear?? The Earth??\n")
            else:
                print("\nI got no idea what that means.")


def cthulhu_room(returned):
    returned = returned
    print("\n\nBehind this door is a portal that sucks you to another realm.\n")
    print("When the spinning stops, you feel an overwhelming heat hitting your body.")
    print("You look up and realize that heat is comming off of the body of an entiy.")
    print('\nWith a eerie dark voice it roars: "I is God Cthulhu!".')
    print("He, it, whatever, stares at you and you go insane.")
    print("\nDo you _flee_ for you life or eat your _head_ ?\n")

    choice = input("> ")

    if "flee" in choice:
        start(returned)
    elif "head" in choice:
        dead("\nWell, that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!\n")
    exit(0)

def start(returned):
    if returned == 0:
        print("\nYou are in a dark room.\n")
        print("There's a door to your\tright")
        print("There's a door to your\tleft")
        print("There's a door in the\tfront\n")
        print("Which one do you take?\n")

    elif returned == 1:
        print("\nYou are back in the dark room again.\n")
        print("There's a door to your\tright")
        print("There's a door to your\tleft")
        print("There's a door in the\tfront\n")
        print("Which one do you take?\n")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right" and (returned == 0):
        cthulhu_room(1)
    elif choice == "right" and (returned == 1):
        cthulhu_room(1)
    elif choice == "front" and not(returned == 1):
        mayan_temple(1)
    else:
        dead("\n\nYou stumble around the room until you starve.")

start(returned)
