# This exercise wanted you the write these points on a index card.
# If I'm using the computer to learn Python, why not do the same with a checklist?

def function_checklist():
    prompt = "Press ENTER to continue \n"

    print('''Which checklist do you want to use?

    1. When you MAKE a function?
    2. When you RUN a fucntion?

    3. Exit (CTRL + C)
    ''')

    checklist_answer = input("Type in: 1, 2 or 3: ")
    if checklist_answer == "1":

        print("\nTHIS IS A CHECKLIST FOR MAKING A FUNCTION\n")

        print("Did you start your function definition with def?: ")
        input(prompt)
        print("Does your function name have only charachters and _(underscore) characters?")
        input(prompt)
        print("Did you put an open parenthesis ( right afther te function name?")
        input(prompt)
        print("Did you put your arguments after the parenthesis ( separated by commas?")
        input(prompt)
        print("Did you make each argument unique (meaning no duplicated names?)")
        input(prompt)
        print("Did you put a close parenthesis and a colon ): afther the argumetns?")
        input(prompt)
        print("Did you indent all lines of code you want in the function four spaces? No more, no less.")
        input(prompt)
        print('Did you "end" your function by going back to writing with no indent (dedenting we call it)? ')
        input(prompt)

        print("\n\nThis is the end of the checklist!\n\nGoodbye!\n\n ")

    elif checklist_answer == "2":

        print("\nTHIS IS A CHECKLIST FOR RUNNING A FUNCTION\n")
        print('When you run ("use" or "call") a function, check these things:\n\n')

        print("Did you call/use/run this function by typing its name?")
        input(prompt)
        print("Did you put the ( character after the name to run it?")
        input(prompt)
        print("Did you put the values you want into the parenthesis separated by commas?")
        input(prompt)
        print("Did you end the function call with a ) character?")
        input(prompt)

        print("\n\nThis is the end of the checklist!\n\nGoodbye!\n\n ")

    elif checklist_answer == "3":
        print("\nGoodbye!\n\n")

    else:
        if checklist_answer != ("1" or "2" or "3"):
            print("\nYou've enterd the wrong answer.\nRestart the the program to try again!\n\nGoodbye!!\n\n")

function_checklist()
