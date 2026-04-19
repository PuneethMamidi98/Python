# Student grade manager
students_list = []

try:
    with open("students.txt","r") as file:
        for line in file:
            parts = line.strip().split(",")
            students_list.append({
                "name" : parts[0],
                "grade" : int(parts[1])
            })
except FileNotFoundError:
    pass            

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
    option = 0 # default value
    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Please enter valid option!")    

    if option == 1:
        try:
            student_name = input("Enter name: ")
            if student_name == "":
                print("Please enter name ")
            else:        
                student_grade = int(input("Enter grade: "))
                if student_grade < 0 or student_grade > 100:
                    print("Grade must be between 0 and 100")
                else:
                    students = {}
                    students["name"] = student_name
                    students["grade"] = student_grade
                    students_list.append(students)
                    with open("students.txt","a") as file:
                        file.write(f"{student_name},{student_grade}\n")
                    print("Student added successfully")    
        except ValueError:
            print("Please Enter valid grade")
        except FileNotFoundError:
            print("File Not found")  

                 
    elif option == 2:
        total = 0
        if len(students_list) == 0:
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



