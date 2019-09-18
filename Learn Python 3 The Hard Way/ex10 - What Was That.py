# This example lets you use \t. Insted of \n (a newline), \t is used for tabs.
tabby_cat = "\tI'm tabbed in."
persina_cat = "I'm split\non a line"


# The first '\' is an escape sequence that lets you use the second '\'.
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
# I created this variables to test some escape sequences and print them out.

## The \v doesn't work in Windows Powershell, That's why u artifically used
## spaces to demonstrate the effects of \v escape sequence.

escape_sequences= '''
ESCAPE SEQUENCES (sme of them)


\tThe \\a
\tASCII BELL (BELL)

Strings with \\a in them will let Python make an sound. \a
That's the sound you heard when you opened this .py file. Restart this file and
listen you'll hear the sound.


\tThe \\b
\tASCII BACKSPACE (BS)

The \\b wil act as a backspace inside a string.
The string ('1234\\b567') will result in: 1234\b567.


\tThe \\f
\tASCII FORMFE\fED (FF)


\tThe \\r
\tCARRIAGE RETURN (CR)

Characters AFTHER the \\r will replace the characters BEFORE the \\r.
("This part of the string will be deleted\\rThis part has been REPLACED.")
("This part of the string will be deleted\r("This part has been REPLACED.")


\tThe \\t
\tHORIZONALT TAB (TAB)

Characters afther the \\t will be tabbed. No so hard to understand. It's just
like you would click on the TAB button on you keyboard for that same reason.

\tThe \\v
\tASCII VERTIAL TAB (VT)

The \\v is also a TAB but it will add a newline.
Example: This is a normal line with
                                    \\v code that newline / TABS this text.

'''
# The print function prints out all de values in the above variables.
## I commented these out myself because the escape sequences are more important.

## print(tabby_cat)
## print(persina_cat)
## print(backslash_cat)
## print(fat_cat)
print("*" * 80)
print(escape_sequences)
print("*" * 80)
