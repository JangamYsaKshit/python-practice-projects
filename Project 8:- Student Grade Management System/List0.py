
# 1. Basic Project – Student Grade Management System

# db
student_marks_DB = []
student_id_number = 0


# Main Code
while True:

    print()
    print("===== STUDENT GRADE MANAGER =====")
    print()
    print("1. Add Marks")
    print("2. Display Marks")
    print("3. Update Marks")
    print("4. Delete Marks")
    print("5. Calculate Statistics")
    print("6. Grade Classification")
    print("7. Sort Marks")
    print("8. Exit")
    print()

    # User Input
    user_menu_input = int(input("Enter Menu Choice: "))


    # 1. Add Marks
    if user_menu_input == 1:

        # Student Details.
        student_name = str(input("Enter Student Name: ")).title()

        if any(student[1] == student_name for student in student_marks_DB):
            print("Error, Student Already Exist")

        else:
            student_class = int(input("Enter Student Class: "))
            student_marks = float(input("Enter Student Marks: "))

            if student_marks < 0 or student_marks > 100:
                print("Error, Marks Must Be Between 0 and 100")

            else:
                student_id_number += 1

                student_marks_DB.append([
                    student_id_number,
                    student_name,
                    student_class,
                    student_marks
                ])

                print("Details Update Successfully.")

        print()


    # 2. Display Marks
    elif user_menu_input == 2:

        if len(student_marks_DB) == 0:
            print("No Data Exist!!!")

        else:
            for display_details in student_marks_DB:
                std_id = display_details[0]
                std_name = display_details[1]
                std_class = display_details[2]
                std_marks = display_details[3]

                print(
                    "Student ID:", std_id,
                    "| Student Name:", std_name,
                    "| Student Class:", std_class,
                    "| Student Marks:", std_marks
                )


    # 3. Update Marks
    elif user_menu_input == 3:

        if len(student_marks_DB) == 0:
            print("No Data Exist!!!")

        else:
            # Input Student Name For Update
            student_name_input = str(input("Enter Student Name: ")).title()

            student_found = False

            for search_student_name in student_marks_DB:

                if search_student_name[1] == student_name_input:
                    print("Student Found.")
                    student_found = True

                    # Input New Marks
                    new_marks = float(input("Enter New Marks: "))

                    if new_marks < 0 or new_marks > 100:
                        print("Error, Marks Must Be Between 0 and 100")

                    else:
                        search_student_name[3] = new_marks
                        print("Update Successfully.")

                    break

            if not student_found:
                print("Data Not Found")


    # 4. Delete Marks
    elif user_menu_input == 4:

        if len(student_marks_DB) == 0:
            print("No Data Exist!!!")

        else:
            # Input Student Name for Delete
            student_delete_search = str(input("Enter Student Name: ")).title()

            student_found = False

            for delete_student_details in student_marks_DB:

                if delete_student_details[1] == student_delete_search:
                    print("Student Found!!")

                    student_marks_DB.remove(delete_student_details)

                    print("Data Delete Successfully.")
                    student_found = True
                    break

            if not student_found:
                print("Data Not Found")


    # 5. Calculate Statistics
    elif user_menu_input == 5:

        if len(student_marks_DB) == 0:
            print("No Data Exist!!!")

        else:
            print()
            print("Student Performance Statistics")
            print("______________________________")

            total_student = len(student_marks_DB)

            # Extract Student Marks
            marks_list = []

            for student in student_marks_DB:
                marks_list.append(student[3])

            print("Total Students:", total_student)

            # Total Marks
            total_marks = sum(marks_list)
            print("Total Marks:", total_marks)

            # Average Marks
            average_marks = total_marks / total_student
            print("Average Marks:", average_marks)

            # Lowest Marks
            lowest_mark = min(marks_list)

            for student in student_marks_DB:
                if student[3] == lowest_mark:
                    print("Lowest Marks:", lowest_mark)
                    print("Student Name:", student[1])
                    break

            # Highest Marks
            highest_mark = max(marks_list)

            for student in student_marks_DB:
                if student[3] == highest_mark:
                    print("Highest Marks:", highest_mark)
                    print("Student Name:", student[1])
                    break

            # Pass and Fail Count
            passed_student = 0
            failed_student = 0

            for marks in marks_list:

                if marks >= 60:
                    passed_student += 1

                else:
                    failed_student += 1

            print("Passed Students:", passed_student)
            print("Failed Students:", failed_student)

            # Pass Percentage
            pass_percentage = (passed_student / total_student) * 100

            print("Pass Percentage:", pass_percentage, "%")


    # 6. Grade Classification
    elif user_menu_input == 6:

        if len(student_marks_DB) == 0:
            print("No Data Exist!!!")

        else:
            print()
            print("Student Grade Classification")
            print("_____________________________")

            for student in student_marks_DB:

                student_marks = student[3]

                if student_marks >= 90:
                    grade = "A"

                elif student_marks >= 80:
                    grade = "B"

                elif student_marks >= 70:
                    grade = "C"

                elif student_marks >= 60:
                    grade = "D"

                else:
                    grade = "F"

                print(
                    "Student Name:", student[1],
                    "| Marks:", student_marks,
                    "| Grade:", grade
                )


    # 7. Sort Marks
    elif user_menu_input == 7:

        if len(student_marks_DB) == 0:
            print("No Data Exist!!!")

        else:
            print()
            # Ask the user which order they want:
            print("1. Show Result In Ascending Order.")
            print("2. Show Result In Descending Order.")

            # User order input
            order_input = int(input("Enter Menu Choice: "))

            # Extract Student Marks
            marks_list = []

            for student in student_marks_DB:
                marks_list.append(student[3])

            if order_input == 1:
                print("Result In Ascending Order.")
                print(sorted(marks_list))

            elif order_input == 2:
                print("Result In Descending Order.")
                print(sorted(marks_list, reverse=True))

            else:
                print("Error, You Entered Wrong Menu Number.")


    # 8. Exit
    elif user_menu_input == 8:
        print("Exit")
        break

    else:
        print("Error, You Entered Wrong Menu Number.")
