# Project 6:- Simple Banking System
# Project Goal:- The goal of this project is to build a console-based banking system that allows users to create and manage bank accounts. 
               # The project is  to improve  Python programming logic and problem-solving skills.


# Start # 
# DB Type:- Dict
account_details = {}


# Main Menu
while True:
    print()
    print("===== BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Search Account")
    print("7. View All Accounts")
    print("8. Exit")
    print()

    user_menu_choice = int(input("Enter Your Choice: "))


    # 1. Create Acoount
    if user_menu_choice == 1:

        user_name = str(input("Enter Your Name: ")).title()
        user_account_type = str(input("Enter Account Type: ")).title()
        user_inital_deposit = float(input("Enter Initial deposit: "))


        if user_name not in account_details and user_inital_deposit > 0:
            account_details[user_name] = {
                "Account Type" : user_account_type,
                "Initial Deposit" : user_inital_deposit
            }

        else:
            print("Error, Data Already Exist OR Initial Deposit is in Negative!!!")
            print("Please Enter Correct Details.")


    # 2. View Account
    elif user_menu_choice == 2:

        if len(account_details) == 0:
            print("Error, No Data Found!!!")

        else:
            for name, type, deposit in account_details.items():
                print("Account Name:", name , "|", "Account Type:", type, "|", "Amount:",deposit)


    # 3. Deposit Money
    elif user_menu_choice == 3:

        # Asking for Account Name
        user_account_name = str(input("Enter Account Holder Name")).title()

        # Searching For Account Name In The DB
        if user_account_name in account_details:
            print("Account Found")
            for user_details in user_account_name:
                account_name = user_details[0]
                account_type = user_details[1]
                print(
                    "Account Name:", account_name, "|", "Account Type", account_type, sep="\n"
                )

            amount_deposit = float(input("Enter Deposit Amount: "))

            if amount_deposit > 0:
                account_details[user_inital_deposit] += amount_deposit
                print("Deposit Successful")
                print("Balance:",account_details[user_inital_deposit])

            else:
                print("Invalid Deposit Amount!")

        else:
            print("Error, Data Not Found!!")


    # 4. Withdraw Money
    elif user_menu_choice == 4:

        # Asking Account Name 
        user_account_name = str(input("Enter Account Holder Name:")).title()

        # Searching For Account Name In DB
        if user_account_name in account_details:
            print("Account Found")
            for user_details in user_account_name:
                account_name = user_details[0]
                account_type = user_details[1]
                print(
                    "Account Name:", account_name, "|", "Account Type:", account_type, sep="\n"
                )

            amount_withdraw = float(input("Enter Withdrawal Amount: "))

            if amount_withdraw < account_details[user_inital_deposit]:
                account_details[user_inital_deposit] -= amount_withdraw
                print("Withdrawal Successfully.")
                print("Balance:", account_details[user_inital_deposit])

            else:
                print("Invalid Withdraw Amount")

        else:
            print("Error, Data Not Found!!")


    # 5. Check Balance
    elif user_menu_choice == 5:

        # Asking Account Name
        user_account_name = str(input("Enter Account Holder Name:")).title()

        # Searching For Account Name In DB
        if user_account_name in account_details:
            print("Account Found")
            for user_details in user_account_name:
                account_name = user_details[0]
                account_type = user_details[1]
                account_balance = user_details[2]
                print(
                    "Account Name:", account_name, "|", "Account Type", account_type, "|", "Balance:", account_balance, sep="\n" 
                )

        else:
            print("Error, Data Not Found!!")           


    # 6. Search Account
    elif user_menu_choice == 6:
        
        # Asking Account Name
        user_account_name = str(input("Enter Account Holder Name:")).title()

        # Searching For Account Name In DB
        if user_account_name in account_details:
            print("Account Found")
            for user_details in user_account_name:
                account_name = user_details[0]
                account_type = user_details[1]
                account_balance = user_details[2]
                print(
                    "Account Name:", account_name, "|", "Account Type", account_type, "|", "Balance:", account_balance, sep="\n" 
                )

        else:
            print("Error, Data Not Found!!")

    
    # 7. View All Accounts  
    elif user_menu_choice == 7:

        if len(account_details) == 0:
            print("Error, Data Not Found!!!")

        else:
            print("Account Details")
            print("...............")
            for user_details in user_account_name:
                account_name = user_details[0]
                account_type = user_details[1]
                account_balance = user_details[2]
                print(
                    "Account Name:", account_name, "|", "Account Type", account_type, "|", "Balance:", account_balance, sep="\n" 
                )


    # 8. Exit
    elif user_menu_choice == 8:
        print("Exit")
        break


    else:
        print("Invalid Menu choice")                 