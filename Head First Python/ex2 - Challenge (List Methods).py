# phrase = "Don't panic!"
# plist = list(phrase)
# print(phrase)
# print(plist)

#
#
#
# Your code here
#
#
#

# new_phrase = ''.join(plist)
# print(plist)
# print(new_phrase)

####################################################
########### Below is code from MdeFrance ###########
####################################################

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.clear()
for chr in 'no tap':        # I came up with this
    plist.append(chr)

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

####################################################
###### Below is the answer from the book ... ######
####################################################

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
