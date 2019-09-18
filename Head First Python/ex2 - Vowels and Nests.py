vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Give me a word to show you its vowels :> ')
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowels in found:
    print(vowels)
