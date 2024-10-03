
#shopping_list = input ("enter your shopping list:")
###shopping_list = [shopping_list]
###print(shopping_list)
while True:
    action = input("""What would you like to do?

                                  Enter 1 to add item

                                  Enter 2 to remove item

                                  Enter 3 to leave the list:\n""")

    if action =="1":

        add(action)

    elif action =="2":

        remove(action)

    else:

        print("Have a nice day!")

        break