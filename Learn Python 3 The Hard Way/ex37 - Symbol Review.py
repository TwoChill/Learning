import random
import time

name = "Boolean Expression Quiz"

# Dictonary with questions on the LEFT and the answers to the Right.
dic_quiz = {
'"as"?': 'part of the with-as statement',
'"assert"?': 'assert that something is true',
'"class"?': 'define a class',
'"del"?': 'delete from a dictionary',
'"exec"?': 'runs a string as python',
'"finally"?': 'finally runs code not matter what',
'"from"?': 'import a specific part of a module',
'"global"?': 'declare that you want a global variable',
'"import"?': 'imports a module',
'"is"?': 'to test equality',
'"lambda"?': 'creates a short anonymous function',
'"pass"? ': 'skips a block of code',
'"with"?': 'part of the with-as statement',
'"yield"?': 'pauses code and returns to caller',

'True':'true',
'False':'false',
'None':'none',
'bytes':"x = b'hallo'",
'strings':'strings',
'numbers':'numbers',
'floats':'floats',
'lists':'lists',
'dicts':'dicts',

'"\\"': 'backslash',
"\\'": 'single-quote',
'\\"': 'double-quotes',
'"\\a"': 'bell',
'"\\b"': 'backspace',
'"\\f"': 'formfeed',
'"\\n"': 'newline',
'"\\r"': 'carriage',
'"\\t"': 'tab',
'"\\v"': 'vertical tab',

'%d':'placeholder for decimal numbers',
'%i':'placeholder for decimal numbers',
'%o':'placeholder for octal numbers',
'%u':'placeholder for unsigned decimal numbers',
'%x':'placeholder for hexadecimal lowercase',
'%X':'placeholder for hexadecimal uppercase',
'%e':"placeholder for exponential notation, lowercase 'e'",
'%E':"placeholder for exponential notation, uppercase 'E'",
'%f':'placeholder for floating point real number',
'%F':'placeholder for floating point real number',
'%g':'placeholder for floating point real number but shorter',
'%G':'placeholder for floating point real number but shorter',
'%c':'placeholder for character format',
'%r':'placeholder for repr (debugging format)',
'%s':'placeholder for strings',
'%%':'placeholder for the % sign',
}

print("\n")
print("=" * len(name),f"\n{name}")
print("=" * len(name))


def range_a(string):
    a = string[0]
    return a

def range_b(string):
    b = string[1]
    return b

def rapport():
            print(f'''
      ==================================
      Boolean Expression Quiz -  Results:
      ==================================
     |       Correct Answerd:    {correct_answerd}      |
     |       Incorrect Answerd:  {incorrect_answerd}      |
     |       Total Questions:    {total_answerd}      |
     |                                  |
     |       Your Grade:         {grade}      |
      ==================================
    ''')
            print("Press CTRL + C to quit.")
            try:
                time.sleep(15)
                exit()
            except:
                if KeyboardInterrupt:
                    exit()

def rapport_2():
            print(f'''2
      ==================================
      Boolean Expression Quiz -  Results:
      ==================================
     |       Correct Answerd:    {correct_answerd}      |
     |       Incorrect Answerd:  {incorrect_answerd}      |
     |       Total Questions:    {total_answerd}     |
     |                                  |
     |       Your Grade:         {grade}      |
      ==================================
    ''')
            print("Press CTRL + C to quit.")
            try:
                time.sleep(15)
                exit()
            except:
                if KeyboardInterrupt:
                    exit()

def quit():
    if ((correct_answerd > 10) or (incorrect_answerd > 10)) or (total_answerd > 10):
        try:
            grade = int(correct_answerd * 10 / total_answerd)
        except ZeroDivisionError:
            grade = 0
        rapport_2()
    else:
        try:
            grade = int(correct_answerd * 10 / total_answerd)
        except ZeroDivisionError:
            grade = 0
        rapport()



randomnr = random.randint(0,26)

correct_answerd = 0
total_answerd = 0
incorrect_answerd = total_answerd - correct_answerd
grade = 0

# Source: quora.com/# How-do-I-convert-a-dictionary-to-a-list-in-Python
list_value = [v for v in dic_quiz]

all_questions  = 0,48
keywords = 0,13
data_types = 14,22
string_escape_sequence = 23,32
old_Style_string_formats = 33,48

# This print block is to prompt user to choose a catagory.
try:
    ranges = int(input(('''
    Which do you want to learn?
    ===========================

     1. All Questions
     2. Keywords
     3. Data Types
     4. String Escape Sequence
     5. Old Style String Formats

    :> ''')))

    # This block is used to 'convert' the users chooice,
    # to the corrospondig range our program uses.
    if ranges == 1:
        print("\n\t:> All Questions")
        ranges = all_questions
    elif ranges == 2:
        print("\n\t:> Keywords")
        ranges = keywords
    elif ranges == 3:
        print("\n\t:> Data Types")
        ranges = data_types
    elif ranges == 4:
        print("\n\t:> String Escape Sequence")
        ranges = string_escape_sequence
    elif ranges == 5:
        print("\n\t:> Old Style String Formats")
        ranges = old_style_string_formats
    elif ranges == 6:
        print("\n\t:> Operators")
        ranges = operators
except ValueError:
    print("\n\t:> 2All Questions")
    ranges = all_questions

print("\n")
print("=" * 32)
print("Type 'quit' or 'result' to exit!")
print("=" * 32)

while True:
    # reminder_count is used to skip the 'remember to type quit' print function twice.
    previous_randomnr = randomnr
    reminder_count = 0

    # Random number generated which correlates to a random question being asked.
    randomnr = random.randint(range_a(ranges),range_b(ranges))

    # This will prevent the program from asking the same question.
    if (previous_randomnr == randomnr) and (reminder_count == 1):
        reminder_count == 0
        continue
    elif previous_randomnr == randomnr:
        print("Type 'quit' or 'result' to exit!")
        reminder_count += 1
        continue

    question = list_value[randomnr]

    print("\n\nQuestion:\t-->\t{}".format(question))
    try:
        answer = input("Description?:\t-->\t").lower()
    except:
        if KeyboardInterrupt:
            exit()
    if (answer == 'quit') or (answer == 'result'):
        quit()

    elif answer == dic_quiz.get(question):
        print("\n\n\t\t\t\tCORRECT!\n\t\t\t\t========")
        correct_answerd += 1
        total_answerd += 1
        previous_randomnr = randomnr

        try:
            grade = int(correct_answerd * 10 / total_answerd)
        except ZeroDivisionError:
            grade = 0

    elif answer != dic_quiz.get(question):
        print("\n\n\t\t\t\tINCORRECT!!\n\t\t\t\t===========")
        print("\nCorrect answer:\t-->\t\t", dic_quiz.get(question).upper())
        print("\t\t\t\t", ("=" * len(dic_quiz.get(question))))
        total_answerd += 1
        previous_randomnr = randomnr

        try:
            grade = int(correct_answerd * 10 / total_answerd)
        except ZeroDivisionError:
            grade = 0
    else:
        previous_randomnr = randomnr

        try:
            grade = int(correct_answerd * 10 / total_answerd)
        except ZeroDivisionError:
            grade = 0

        continue
