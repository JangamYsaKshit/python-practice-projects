# Project 1 — Personal Shopping List Manager
# Project Goal: Build a small console program that allows a user to create and manage their shopping list.

# Empty list
Shopping_List = []

# Menu
while True:
    print()
    print("------Menu------")
    print("1 - Add Item")
    print("2 - View Item")
    print("3 - Remove Item")
    print("4 - View Total Item")
    print("5 - Exit")
    print()

    # User Input
    user_menu = int(input("Enter A Number: "))

    # Add Item
    if user_menu == 1:
        count = 0
        user_item_name = input("Enter Item Name: ")
        if user_item_name == "":
            print("Error! Item Name Cannot Be Empty")

        elif user_item_name in Shopping_List:
            print("Item Already In The List")

        else:
            Shopping_List.append(user_item_name)
            print("Item Added Successfully")

    # View Item
    elif user_menu == 2:
        if len(Shopping_List) == 0:
            print("Error! Add Item To View")

        else:
            print("Your Item")
            count = 1
            for items in Shopping_List:
                print(count, "-", items)
                count += 1

    # Remove Item
    elif user_menu == 3:
        remove_item = input("Enter Item Name To Remove: ")

        if remove_item in Shopping_List:
            Shopping_List.remove(remove_item)
            print(f"'{remove_item}' removed.")

        else:
            print("Error! Item Not Found")

    # View Total Item
    elif user_menu == 4:
        print("Total Item:", len(Shopping_List))

    # Exit
    elif user_menu == 5:
        print("Exit")
        break

    # Invalid Menu Choice
    else:
        print("Error! Invalid Menu Choice")
