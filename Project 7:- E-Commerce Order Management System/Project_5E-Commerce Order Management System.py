
# Project_5_E-Commerce Order Management System.py

# Project Goal
# Manage products, customers, orders, inventory, and sales using Python.

# 3 DB
Products = []
Customers = []
Orders = []

# Unique IDs
unique_product_id = 100
unique_customer_id = 100
unique_order_id = 1000


# Menu Options
while True:

    print()
    print("===== E-COMMERCE ORDER MANAGEMENT =====")
    print()
    print("1. Add Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Remove Product")
    print("6. Create Customer Order")
    print("7. View All Orders")
    print("8. Search Order")
    print("9. Update Order")
    print("10. Cancel Order")
    print("11. View Sales Summary")
    print("12. View Inventory Summary")
    print("13. Exit")
    print()

    user_menu_choice = int(input("Enter Menu Number: "))

    # 1. Add Product
    if user_menu_choice == 1:

        product_name = input("Enter Product Name: ").title().strip()
        product_category = input("Enter Product Category: ").title().strip()
        product_price = float(input("Enter Product Price: "))
        product_stock = int(input("Enter Product Quantity: "))

        if product_name == "" or product_category == "":
            print("Product Name and Category cannot be empty.")

        elif product_price <= 0 or product_stock < 0:
            print("Invalid Price or Stock Quantity.")

        else:
            unique_product_id += 1

            Products.append((
                unique_product_id,
                product_name,
                product_category,
                product_price,
                product_stock
            ))

            print("Product Added Successfully.")
            print("Product ID:", unique_product_id)

    # 2. View All Products
    elif user_menu_choice == 2:

        if len(Products) == 0:
            print("No Products Available.")

        else:
            print()
            print("===== ALL PRODUCTS =====")

            for product in Products:

                product_id = product[0]
                product_name = product[1]
                product_category = product[2]
                product_price = product[3]
                product_stock = product[4]

                print(
                    "Product ID:", product_id,
                    "| Name:", product_name,
                    "| Category:", product_category,
                    "| Price: €", product_price,
                    "| Stock:", product_stock
                )

    # 3. Search Product
    elif user_menu_choice == 3:

        if len(Products) == 0:
            print("No Products Available.")

        else:
            search_product_id = int(input("Enter Product ID: "))

            product_found = False

            for product in Products:

                if product[0] == search_product_id:

                    product_found = True

                    print()
                    print("Product Found")
                    print("Product ID:", product[0])
                    print("Product Name:", product[1])
                    print("Product Category:", product[2])
                    print("Product Price: €", product[3])
                    print("Product Stock:", product[4])

                    break

            if product_found == False:
                print("Product Not Found.")

    # 4. Update Product
    elif user_menu_choice == 4:

        if len(Products) == 0:
            print("No Products Available.")

        else:
            update_product_id = int(input("Enter Product ID: "))

            product_found = False

            for index, product in enumerate(Products):

                if product[0] == update_product_id:

                    product_found = True

                    updated_product = list(product)

                    print()
                    print("Product Found")
                    print("Product ID:", product[0])
                    print("Product Name:", product[1])
                    print("Product Category:", product[2])
                    print("Product Price: €", product[3])
                    print("Product Stock:", product[4])

                    while True:

                        print()
                        print("===== UPDATE PRODUCT =====")
                        print("1. Product Name")
                        print("2. Product Category")
                        print("3. Product Price")
                        print("4. Product Stock Quantity")
                        print("5. Save and Exit")

                        update_menu_choice = int(input("Select Field: "))

                        if update_menu_choice == 1:

                            new_product_name = input("Enter New Product Name: ").title().strip()

                            if new_product_name != "":
                                updated_product[1] = new_product_name
                                print("Product Name Updated.")
                            else:
                                print("Product Name Cannot Be Empty.")

                        elif update_menu_choice == 2:

                            new_product_category = input("Enter New Category: ").title().strip()

                            if new_product_category != "":
                                updated_product[2] = new_product_category
                                print("Product Category Updated.")
                            else:
                                print("Category Cannot Be Empty.")

                        elif update_menu_choice == 3:

                            new_product_price = float(input("Enter New Price: "))

                            if new_product_price > 0:
                                updated_product[3] = new_product_price
                                print("Product Price Updated.")
                            else:
                                print("Price Must Be Greater Than Zero.")

                        elif update_menu_choice == 4:

                            new_product_stock = int(input("Enter New Stock Quantity: "))

                            if new_product_stock >= 0:
                                updated_product[4] = new_product_stock
                                print("Stock Quantity Updated.")
                            else:
                                print("Stock Cannot Be Negative.")

                        elif update_menu_choice == 5:

                            Products[index] = tuple(updated_product)
                            print("Product Details Saved Successfully.")
                            break

                        else:
                            print("Invalid Menu Choice.")

                    break

            if product_found == False:
                print("Product Not Found.")

    # 5. Remove Product
    elif user_menu_choice == 5:

        if len(Products) == 0:
            print("No Products Available.")

        else:
            remove_product_id = int(input("Enter Product ID To Remove: "))

            product_found = False

            for product in Products:

                if product[0] == remove_product_id:

                    product_found = True

                    # Check whether product belongs to an active order
                    active_order_product = False

                    for order in Orders:

                        if order[4] != "Cancelled":

                            for order_item in order[3]:

                                if order_item[0] == remove_product_id:
                                    active_order_product = True

                    if active_order_product:
                        print("Cannot Remove Product. It Belongs To An Active Order.")

                    else:

                        print("Product Found")
                        print("Product Name:", product[1])

                        remove_confirmation = input(
                            "Do You Want To Remove This Product (Yes/No): "
                        ).title()

                        if remove_confirmation == "Yes":
                            Products.remove(product)
                            print("Product Removed Successfully.")

                        elif remove_confirmation == "No":
                            print("Remove Request Cancelled.")

                        else:
                            print("Invalid Confirmation.")

                    break

            if product_found == False:
                print("Product Not Found.")

    # 6. Create Customer Order
    elif user_menu_choice == 6:

        if len(Products) == 0:
            print("No Products Available. Add Products First.")

        else:

            customer_name = input("Enter Customer Name: ").title().strip()
            customer_email = input("Enter Customer Email: ").strip()

            if customer_name == "" or customer_email == "":
                print("Customer Details Cannot Be Empty.")

            else:

                # Check whether customer already exists
                customer_found = False
                customer_id = 0

                for customer in Customers:

                    if customer[2].lower() == customer_email.lower():

                        customer_found = True
                        customer_id = customer[0]
                        break

                if customer_found == False:

                    unique_customer_id += 1
                    customer_id = unique_customer_id

                    Customers.append((
                        customer_id,
                        customer_name,
                        customer_email
                    ))

                # Create order items
                order_items = []
                order_total = 0

                while True:

                    print()
                    print("===== AVAILABLE PRODUCTS =====")

                    for product in Products:

                        print(
                            "ID:", product[0],
                            "| Name:", product[1],
                            "| Price: €", product[3],
                            "| Stock:", product[4]
                        )

                    selected_product_id = int(input("Enter Product ID: "))

                    selected_product_found = False

                    for product_index, product in enumerate(Products):

                        if product[0] == selected_product_id:

                            selected_product_found = True

                            if product[4] <= 0:
                                print("Product Out Of Stock.")

                            else:

                                order_quantity = int(input("Enter Quantity: "))

                                if order_quantity <= 0:
                                    print("Quantity Must Be Greater Than Zero.")

                                elif order_quantity > product[4]:
                                    print("Insufficient Stock.")
                                    print("Available Stock:", product[4])

                                else:

                                    item_total = product[3] * order_quantity

                                    order_items.append((
                                        product[0],
                                        product[1],
                                        product[3],
                                        order_quantity
                                    ))

                                    order_total += item_total

                                    # Reduce product stock
                                    updated_product = list(product)
                                    updated_product[4] -= order_quantity

                                    Products[product_index] = tuple(updated_product)

                                    print("Product Added To Order.")
                                    print("Item Total: €", round(item_total, 2))

                            break

                    if selected_product_found == False:
                        print("Product Not Found.")

                    add_more_products = input(
                        "Do You Want To Add More Products (Yes/No): "
                    ).title()

                    if add_more_products != "Yes":
                        break

                if len(order_items) > 0:

                    unique_order_id += 1

                    order_status = "Pending"

                    Orders.append((
                        unique_order_id,
                        customer_id,
                        customer_name,
                        order_items,
                        round(order_total, 2),
                        order_status
                    ))

                    print()
                    print("===== ORDER CREATED SUCCESSFULLY =====")
                    print("Order ID:", unique_order_id)
                    print("Customer Name:", customer_name)
                    print("Order Total: €", round(order_total, 2))
                    print("Order Status:", order_status)

                else:
                    print("Order Not Created. No Products Selected.")

    # 7. View All Orders
    elif user_menu_choice == 7:

        if len(Orders) == 0:
            print("No Orders Available.")

        else:

            print()
            print("===== ALL ORDERS =====")

            for order in Orders:

                print()
                print("Order ID:", order[0])
                print("Customer ID:", order[1])
                print("Customer Name:", order[2])
                print("Order Status:", order[5])

                for order_item in order[3]:

                    print(
                        "Product ID:", order_item[0],
                        "| Product Name:", order_item[1],
                        "| Price: €", order_item[2],
                        "| Quantity:", order_item[3]
                    )

                print("Order Total: €", order[4])
                print("-----------------------------")

    # 8. Search Order
    elif user_menu_choice == 8:

        if len(Orders) == 0:
            print("No Orders Available.")

        else:

            search_order_id = int(input("Enter Order ID: "))

            order_found = False

            for order in Orders:

                if order[0] == search_order_id:

                    order_found = True

                    print()
                    print("Order Found")
                    print("Order ID:", order[0])
                    print("Customer ID:", order[1])
                    print("Customer Name:", order[2])
                    print("Order Status:", order[5])

                    for order_item in order[3]:

                        print(
                            "Product ID:", order_item[0],
                            "| Product Name:", order_item[1],
                            "| Price: €", order_item[2],
                            "| Quantity:", order_item[3]
                        )

                    print("Order Total: €", order[4])

                    break

            if order_found == False:
                print("Order Not Found.")

    # 9. Update Order
    elif user_menu_choice == 9:

        if len(Orders) == 0:
            print("No Orders Available.")

        else:

            update_order_id = int(input("Enter Order ID: "))

            order_found = False

            for order_index, order in enumerate(Orders):

                if order[0] == update_order_id:

                    order_found = True

                    if order[5] == "Cancelled":
                        print("Cannot Update A Cancelled Order.")

                    else:

                        print("Current Status:", order[5])
                        print()
                        print("1. Pending")
                        print("2. Shipped")
                        print("3. Delivered")

                        new_status_choice = int(input("Select New Status: "))

                        if new_status_choice == 1:
                            new_order_status = "Pending"

                        elif new_status_choice == 2:
                            new_order_status = "Shipped"

                        elif new_status_choice == 3:
                            new_order_status = "Delivered"

                        else:
                            new_order_status = ""

                        if new_order_status != "":

                            updated_order = list(order)
                            updated_order[5] = new_order_status

                            Orders[order_index] = tuple(updated_order)

                            print("Order Status Updated Successfully.")

                        else:
                            print("Invalid Status Choice.")

                    break

            if order_found == False:
                print("Order Not Found.")

    # 10. Cancel Order
    elif user_menu_choice == 10:

        if len(Orders) == 0:
            print("No Orders Available.")

        else:

            cancel_order_id = int(input("Enter Order ID To Cancel: "))

            order_found = False

            for order_index, order in enumerate(Orders):

                if order[0] == cancel_order_id:

                    order_found = True

                    if order[5] == "Cancelled":
                        print("Order Already Cancelled.")

                    elif order[5] == "Delivered":
                        print("Delivered Orders Cannot Be Cancelled.")

                    else:

                        print("Order Found")
                        print("Customer:", order[2])
                        print("Order Total: €", order[4])

                        cancel_confirmation = input(
                            "Do You Want To Cancel This Order (Yes/No): "
                        ).title()

                        if cancel_confirmation == "Yes":

                            # Restore product stock
                            for order_item in order[3]:

                                for product_index, product in enumerate(Products):

                                    if product[0] == order_item[0]:

                                        updated_product = list(product)
                                        updated_product[4] += order_item[3]

                                        Products[product_index] = tuple(updated_product)

                                        break

                            updated_order = list(order)
                            updated_order[5] = "Cancelled"

                            Orders[order_index] = tuple(updated_order)

                            print("Order Cancelled Successfully.")
                            print("Product Stock Restored.")

                        elif cancel_confirmation == "No":
                            print("Order Cancellation Request Cancelled.")

                        else:
                            print("Invalid Confirmation.")

                    break

            if order_found == False:
                print("Order Not Found.")

    # 11. View Sales Summary
    elif user_menu_choice == 11:

        if len(Orders) == 0:
            print("No Orders Available.")

        else:

            total_orders = len(Orders)
            pending_orders = 0
            shipped_orders = 0
            delivered_orders = 0
            cancelled_orders = 0
            total_sales = 0
            highest_order_amount = 0

            for order in Orders:

                if order[5] == "Pending":
                    pending_orders += 1

                elif order[5] == "Shipped":
                    shipped_orders += 1

                elif order[5] == "Delivered":
                    delivered_orders += 1

                elif order[5] == "Cancelled":
                    cancelled_orders += 1

                if order[5] != "Cancelled":

                    total_sales += order[4]

                    if order[4] > highest_order_amount:
                        highest_order_amount = order[4]

            print()
            print("===== SALES SUMMARY =====")
            print("Total Orders:", total_orders)
            print("Pending Orders:", pending_orders)
            print("Shipped Orders:", shipped_orders)
            print("Delivered Orders:", delivered_orders)
            print("Cancelled Orders:", cancelled_orders)
            print("Total Sales: €", round(total_sales, 2))
            print("Highest Order Amount: €", round(highest_order_amount, 2))

    # 12. View Inventory Summary
    elif user_menu_choice == 12:

        if len(Products) == 0:
            print("No Products Available.")

        else:

            total_products = len(Products)
            total_stock_units = 0
            total_inventory_value = 0
            highest_price = 0
            highest_price_product = ""
            low_stock_count = 0

            print()
            print("===== INVENTORY SUMMARY =====")

            for product in Products:

                total_stock_units += product[4]

                total_inventory_value += product[3] * product[4]

                if product[3] > highest_price:
                    highest_price = product[3]
                    highest_price_product = product[1]

                if product[4] <= 5:
                    low_stock_count += 1

                    print(
                        "Low Stock Product:",
                        product[1],
                        "| Available Stock:",
                        product[4]
                    )

            print()
            print("Total Products:", total_products)
            print("Total Stock Units:", total_stock_units)
            print("Total Inventory Value: €", round(total_inventory_value, 2))
            print("Low Stock Products:", low_stock_count)
            print("Highest Price Product:", highest_price_product)
            print("Highest Product Price: €", highest_price)

    # 13. Exit
    elif user_menu_choice == 13:

        print("Thank You For Using E-Commerce Order Management System.")
        break

    # Invalid Menu Choice
    else:
        print("Error! Invalid Menu Choice.")
