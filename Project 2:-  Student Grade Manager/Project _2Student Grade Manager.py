# Project 2 — Student Grade Manager
# Project Goal: Build a console program that allows a user to enter and manage student grades.


# Empty Dist
Student_Grades = {}

# Menu
while True:
    print()
    print("------Menu------")
    print("1 - Add Grades")
    print("2 - View Grades")
    print("3 - View Total Grades")
    print("4 - Calculate Average Grades")
    print("5 - View Highest Grades")
    print("6 - View Lowest Grades")
    print("7 - Exit")
    print()


    # 1 User Input
    user_menu = int(input("Enter A Number: "))

    # Add Grades
    if user_menu == 1:

        student_name = input("Enter Student Name: ")
        student_marks = float(input("Enter Student Grade: "))

        Student_Grades[student_name] = student_marks
        print("Student Added Successfully")


    # 2 View Grades
    elif user_menu == 2:

        if len(Student_Grades) == 0:
            print("Error! Add Student Grades First")

        else:
            for name, marks in Student_Grades.items():
                if marks >= 50 and marks <= 59:
                    grade = "D"

                elif marks >= 60 and marks <= 69:
                     grade = "C"

                elif marks >= 70 and marks <= 79:
                    grade = "B"

                elif marks >= 80 and marks <= 89:
                    grade = "A"

                elif marks >= 90 and marks <= 100:
                    grade = "A+"

                else:
                    grade = "Fail"  

                print("Student Name:", name, "|",
                  "Student Marks:", marks, "|",
                  "Grade:", grade) 


    # 3 View Total Grades
    elif user_menu == 3:
        print("Total Number Of Grade Is: ",len(Student_Grades))


    # 4 Calculate Average Grades
    elif user_menu == 4:

        if len(Student_Grades) == 0:
            print("Error! Add Student Grades First")

        else:
           average_marks = sum(Student_Grades.values()) / len(Student_Grades)
           print("Average Marks:", average_marks)


    # 5 View Highest Grades
    elif user_menu == 5:
        Highest_marks = max(Student_Grades.values())

        for name, marks in Student_Grades.items():
            if marks == Highest_marks:
                print("Student Name:", name, "|", "Student Marks:", marks)


    # 6 View Lowest Grades
    elif user_menu == 6:
        Lowest_marks = min(Student_Grades.values())

        for name, marks in Student_Grades.items():
            if marks == Lowest_marks:
                print("Student Name:", name, "|", "Student Marks", marks)


    # 7 Exit
    elif user_menu == 7:
        print("Exit")
        break


    # For Invalid User Menu Choice
    else:
        print("Invalid Menu Choice")