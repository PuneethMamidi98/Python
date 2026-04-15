# Student grade manager
students_list = []

isBrowersing = True
while isBrowersing :
    # Welcome 
    print("================================")
    print("Welcome to Student Grade Manager")
    print("================================")

    print("1. Add student")
    print("2. View all students")
    print("3. Find top student")
    print("4. Exit")

    option = int(input("Enter your option: "))

    if option == 1:
        student_name = input("Enter name: ")
        student_grade = int(input("Enter grade: "))
        students = {}
        students["name"] = student_name
        students["grade"] = student_grade
        students_list.append(students)
        print("Student added sucessfully")
    elif option == 2:
        total = 0
        if len(student_list) == 0:
            print("No students added yet!")
        else:
            for student in students_list:
                print(f"{student["name"]} - {student["grade"]}")
                total += student["grade"]
            average = round(total / len(students_list))
            print(f"Average grade: {average}")    
    elif option == 3:
        topper = max(students_list, key=lambda k: k["grade"])
        print(f"Top student: {topper["name"]} with {topper["grade"]}")
    elif option == 4:
        print("Goodbye see you again!")
        isBrowersing = False
    else:
        print("Invalid option, please try again!")    



