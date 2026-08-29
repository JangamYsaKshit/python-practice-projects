# Project 3 — To-Do List Manager
# Project Goal: Build a small console application that allows a user to create and manage a list of tasks.


# Empty List 
Tasks = []

# Empty list for Completed Task 
Completed_Tasks = []

while True:
    print()
    print("------Menu------")
    print("1- Add Task")
    print("2- View Tasks")
    print("3- Complete Task")
    print("4- Remove Task")
    print("5- View Total Tasks")
    print("6- View Completed Tasks")
    print("7 - Exit")
    print()


    menu_choice = int(input("Enter Number: "))

    # 1 - Add Task
    if menu_choice == 1:
        Task_name = str(input("Enter Task Name: "))
        if Task_name in Tasks:
            print("Task Already Exist")

        else:
            Tasks.append(Task_name)
            print("Task Added Successfully...")

    # 2 - View Task
    elif menu_choice == 2:

        if len(Tasks) == 0:
            print("Error!! No Task Is Available...")

        else:
            for Task_list in Tasks:
                print(Task_list)

    # 3 - Complete Task
    elif menu_choice == 3:
        completed_task = input("Enter Task Name To Mark Complete: ")

        if completed_task in Tasks:
            Tasks.remove(completed_task)
            Completed_Tasks.append(completed_task)

        else:
            print("Invalid Task")

    # 4 - Remove Task
    elif menu_choice == 4:
        task_to_delete = input("Enter Task Name To Delete")

        if task_to_delete in Tasks:
            Tasks.remove(task_to_delete)
            print("Task Delete Successfully")

        else:
            print("Invalid Task Name")

    # 5 - View Total Tasks
    elif menu_choice == 5:
        print("Total Tasks:", len(Tasks))

    # 6 - View Completed Tasks:
    elif menu_choice == 6:
        print("------Completed Tasks------")
        print(Completed_Tasks)

    # 7 - Exit 
    elif menu_choice == 7:
        print("Exit")
        break 

    else:
        print("Error! Invalid Number")