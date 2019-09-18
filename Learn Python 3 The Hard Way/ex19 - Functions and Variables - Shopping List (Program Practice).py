###############################################################################
print("#" * 35, "\n")

print("PRACTICE FUNCTIONS - SHOPPING LIST\n\n")

print("#" * 35, "\n")

def shopping_list():

    list_name_items = []
    print("Type 'quit' to see the results.\nPress ENTER to add another shopping Item.\n\n")
    print("Name your items for your shopping list:\n\n")

    while True:
        amount_items = len(list_name_items)
        name_items = input("Shopping Item nr." + str(amount_items) + " > ")
        if name_items == "quit":
            break
        list_name_items.append(name_items)

    print(f"\nYou have {amount_items} items in you shopping list.\n")
    print(f"Your list contains:\n{list_name_items}\n")

shopping_list()

print("#" * 35, "\n")
###############################################################################
