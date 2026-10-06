# project 1:- Daily Habit Tracker 
# Goal:- Refresh your Python fundamentals and get your programming flow back.


# Start #
# DB Type: List
habit = []

# DB For Complete Habit Type: List
completed_habits = []

# Main code. 
while True:

    # Menu Options.
    print()
    print("===== Daily Habit Tracker =====")
    print()
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. View Progress")
    print("5. Remove Habit")
    print("6. Exit")
    print()


    # User Menu Input
    user_menu_choice = int(input("Enter your choice: "))


    # 1. Add Habit
    if user_menu_choice == 1:
        habit_name = input("Enter Habit: ").title()

        if habit_name in habit:
            print("Error, habit already Exist")

        else:
            habit.append(habit_name)
            print("Added Successfully.")


    # 2. View Habit
    elif user_menu_choice == 2:

        number = 0

        print("Your Habits")
        print("...........")

        for view_habits in habit:
            print(view_habits)
            number += 1


    # 3. Complete Habit
    elif user_menu_choice == 3:
        number = 0

        user_completed_habit = input("Which Habit Did You Complete: ").title()
        if user_completed_habit not in habit:
            print("Error, Data ot Found, Please Enter Correct Habit")

        else:
            habit.remove(user_completed_habit)
            completed_habits.append(user_completed_habit)

            print("Habit Marked As Completed")
            print(".........................")
            for complete_habit_view in completed_habits:
                print(complete_habit_view)
                number += 1 


    # 4. View Progress
    elif user_menu_choice == 4:
        total_completed = len(completed_habits)
        total_remaining = len(habit)
        total_habits = total_completed + total_remaining

        if total_habits == 0:
            print("No Habits Available")

        else:
            print("Today's Progress")

            total_percentage = (total_completed / total_habits) * 100

            print("Completed:", total_completed)
            print("Remaining:", total_remaining)
            print("Progress:", round(total_percentage), "%")


    # 5. Remove Habit
    elif user_menu_choice == 5:
        remove_habit = input("Enter Habit To Remove: ")

        if remove_habit in habit:
            habit.remove(remove_habit)
            print(remove_habit, "Removed.")

        else:
            print("Error, Data Not Found")


    # 6 Exit
    elif user_menu_choice == 6:
        print("Exit")
        break


    else:
        print("Invalid Menu Choice!")

# End