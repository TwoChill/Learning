# # DICTIONARY
#
# # a dict and print the value of the key!
# ex40_mystuf = {'apple': "I AM APPLES!"}
# # get X from Y. X = 'apples'. Y = ex40_mystuff
# print(ex40_mystuf['apple'])
#
#
# # MODULES
#
# # create a python file with some functions or variables in it and import it like:
# import ex40_mystuff
#
# # Call the module first. And then call the function or varibale to use it.
# ex40_mystuff.apple()
# print(ex40_mystuff.tangerine)
#
# ex40_mystuf['apple']   # DICTIONARY
# ex40_mystuff.apple()    # MODULE AND FUCNTION
# ex40_mystuff.tangerine  # MODULE AND VARIABLE


# # CLASSES
#
#
# class MyStuff(object):
#
#     def __init__(self):
#         self.tangerine = 'And now a thousand years between'
#
#     def apple(self):
#         print('I AM CLASSY APPLES!')
#
#
# var = MyStuff()
# var.apple()
# print(var.tangerine)


# 40.1.4

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bd = Song(["Happy birtyday to you",
                 "I don't want to get sued",
                 "So I'll stop right there"])

bulls_on_parade = Song(["They ral;y around that family",
                        "With pckets full of shells"])

never_rap = Song(["De eerste keer dat ik je zag",
                  "Wist ik niet wie je was",
                  "Maar van waar jij zat",
                  "Zag ik wel jou mooie lach"])

# Using variables instead of lists to see what happends
var1 = "Aan het eind van de show"
var2 = "Zei ik jou toch nog gedag"
var3 = "Wist ik veel"
var4 = "Dat jij ook op mijn school zat"
var5 = var1 + var2 + var3 + var4

stop_it = Song(var5)
stop_it.sing_me_a_song()
# It will print each character on a new line.

never_rap.sing_me_a_song()

happy_bd.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
