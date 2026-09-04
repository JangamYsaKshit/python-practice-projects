# Project 5 — Inventory Management System
# Project Goal: Develop a practical inventory management system using Python while strengthening core programming, problem-solving, and data management skills

# Empty List 
Inventory = []
[]

# ==================================================
# Add Product
# Adds a new product to the inventory after validating
# the product ID and collecting product information.
# ==================================================
def add_fun():
    product_id = int(input("Enter Product_id: "))

    # Check whether the product ID already exists
    if product_id in Inventory:
        print("Invalid, Product Already Exist.")

    # Validate that the product ID is positive
    elif product_id <= 0:
        print("Error") 

    # Get product details from the user
    else:
        product_name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Total Number Of Quantity: "))

        Inventory.append([product_id, product_name, category, price, quantity])
        print("Product Added Successfully.")
        print()


# ==================================================
# View Inventory
# Displays all products currently stored in inventory.
# Shows product ID, name, category, price, and quantity.
# ==================================================
def view_fun():

    if len(Inventory) == 0:
        print("No Data To View.")

    else:
        for product_id, product_name, category, prices, quantity in Inventory:
            print("Product Id:", product_id,
                  "| Product Name", product_name,
                  "| Category", category,
                  "| Price", prices,
                  "| quantity", quantity)


# ==================================================
# Search Product
# Searches for a product using its unique Product ID.
# Displays the product details if a matching ID is found.
# ==================================================
def search_fun():   
    user_search = int(input("ENter Product Id: "))

    for search in Inventory:
        if user_search == search[0]:
            print("Product Id:", search[0],
                  "| Product Name", search[1],
                  "| Category", search[2],
                  "| Price", search[3],
                  "| quantity", search[4])
            break

    else:
        print("Product Id Not Found")


# ==================================================
# Update Product
# Searches for a product by Product ID and allows
# the user to update its name, category, price,
# or quantity.
# ==================================================
def update_fun():
    user_update = int(input("Enter Product Id: "))

    for update_search in Inventory:
        if user_update == update_search[0]:
            print("Product Id:", update_search[0],
                  "| Product Name", update_search[1],
                  "| Category", update_search[2],
                  "| Price", update_search[3],
                  "| quantity", update_search[4]
                  )

            print()
            print("What To Update") 
            print("1 - Product Name")
            print("2 - Category")
            print("3 - Price")
            print("4 - Quantity")
            print()

            user_update_menu = int(input("Enter Menu Number: "))

            if user_update_menu == 1:
                update_product_name = input("Enter New Product Name: ")
                update_search[1] = update_product_name
                print("Update Successfully.")
                print()

            elif user_update_menu == 2:
                update_category = input("Enter New Category: ")
                update_search[2] = update_category
                print("Update Successfully.")
                print()

            elif user_update_menu == 3:
                update_price = float(input("Enter New Product Price: "))
                update_search[3] = update_price
                print("Update Successfully.")
                print()

            elif user_update_menu == 4:
                update_quantity = int(input("Enter New Quantity: "))
                update_search[4] = update_quantity
                print("Update Successfully.")
                print()

            else:
                print("Error Invalid Choice!")

            break

        else:
            print("Error Product Id Not Found!")


# ==================================================
# Remove Product
# Searches for a product using its Product ID and
# removes the complete product record from inventory.
# ==================================================
def remove_fun():
    user_remove = int(input("Enter Product Id: "))

    for user_remove_search in Inventory:
        if user_remove == user_remove_search[0]:
            Inventory.remove(user_remove_search)
            print("Product Removed Successfully.")
            break

    else:
        print("Product Id Not Found!")


# ==================================================
# Sell Product
# Searches for a product by Product ID, validates
# the requested selling quantity, updates stock,
# and calculates the total sale amount.
# ==================================================
def sell_fun():
    user_search_sell_inventory = int(input("ENter Product Id: "))

    for user_sell_product in Inventory:
        if user_search_sell_inventory == user_sell_product[0]:
            print("Product Id:", user_sell_product[0],
                  "| Product Name", user_sell_product[1],
                  "| Category", user_sell_product[2],
                  "| Price", user_sell_product[3],
                  "| quantity", user_sell_product[4]
                  )

            quantity_sell = int(input("How many Quantity do you want to sell?: "))

            if quantity_sell <= 0:
                print("Invalid Quantity!")

            elif quantity_sell > user_sell_product[4]:
                print("Not Enough Stock!")

            else:
                # Subtract sold quantity
                quantity_left = user_sell_product[4] - quantity_sell
                user_sell_product[4] = quantity_left
                        
                # Calculate Total Sale
                total_price = user_sell_product[3] * quantity_sell

                # Display Sale Successful
                print("Sell Successfully.")

                # Display Total Sale Amount
                print("Total Amount:", total_price)

                # Display Remaining Quantity
                print("Quantity Left:", quantity_left)

                break

    else:
        print("Product Id Not Found!")

# ==================================================
# Restock Product
# Searches for a product by Product ID, validates
# the restock quantity, and increases the available
# inventory quantity.
# ==================================================
def restock_fun():
    user_restock_product = int(input("Enter Product Id: "))

    # Display Product Details
    for restock_product in Inventory:
        if user_restock_product == restock_product[0]:
            print("Product Id:", restock_product[0],
                  "| Product Name", restock_product[1],
                  "| Category", restock_product[2],
                  "| Price", restock_product[3],
                  "| quantity", restock_product[4]
                  )

            # Add Restock Quantity
            units_restock = int(input("How many units to restock: "))
            if units_restock <= 0:
                print("Invalid Quantity!")

            else:
                #  Add Restock Quantity
                add_quantity = restock_product[4] + units_restock
                restock_product[4] = add_quantity  # Update Inventory
                print("Restock Successfully.")
                print()

                print("New Quantity:", restock_product[4])

                break

    else:
        print("Product Id Not Fount!")


# ==================================================
# Inventory Statistics
# Calculates and displays overall inventory statistics,
# including total products, total quantity, total value,
# most expensive product, and lowest-stock product.
# ==================================================
def statistics_fun():
    if len(Inventory) == 0:
        print("No Inventory Data!")

    else:
        # 1. Calculate Total Products
        count = 0
        for product in Inventory:
            count += 1
        print("Total Products:", count)


        # 2. Calculate Total Quantity
        total_quantity = 0
        for product in Inventory:
            total_quantity += product[4]
        print("Total Quantity:", total_quantity)


        # 3. Calculate Total Inventory Value
        total_value = 0
        for product in Inventory:
            product_value = product[3] * product[4]
            total_value += product_value
        print("Total Inventory Value:", total_value)


        # 4. Find Most Expensive Product
        most_expensive = Inventory[0]
        for product in Inventory:
            if product[3] > most_expensive[3]:
                most_expensive = product

        print("Most Expensive Product:", most_expensive[1])
        print("Price:", most_expensive[3])


        # 5. Find Lowest Stock Product
        lowest_stock = Inventory[0]
        for product in Inventory:
            if product[4] < lowest_stock[4]:
                lowest_stock = product

        print("Lowest Stock Product:", lowest_stock[1])
        print("Quantity:", lowest_stock[4]) 



# Menu Loop
while True:

    print("========== INVENTORY MANAGEMENT SYSTEM ==========")
    print()
    print("====== Menu ======")
    print("1 - Add Product")
    print("2 - View Inventory")
    print("3 - Search Product")
    print("4 - Update Product")
    print("5 - Remove Product")
    print("6 - Sell Product")
    print("7 - Restock Product")
    print("8 - Inventory Statistics")
    print("9 - Exit")
    print()


    user_menu = int(input("Enter Menu Choice: "))

    # 1 - Add Product
    if user_menu == 1:
        add_fun()

    # 2 - View Inventory
    elif user_menu == 2:
        search_fun()

    # 3 - Search Product
    elif user_menu == 3:
        view_fun()

    # 4 - Update Product
    elif user_menu == 4:
        update_fun()

    # 5 - Remove Product
    elif user_menu == 5:
        remove_fun()

    # 6 - Sell Product
    elif user_menu == 6:
        sell_fun()

    # 7 - Restock Product
    elif user_menu == 7:
        restock_fun()

    # 8 - Inventory Statistics
    elif user_menu == 8:
        statistics_fun()

    # 9 - Exit
    elif user_menu == 9:
        print("Exit")
        break

# ====== END ======
