# Refactored version with funtions

students_list = []

def load_students():
    try:
        with open("students.txt","r") as file:
            for line in file:
                parts = line.strip().split(",")
                students_list.append({
                    "name" : parts[0],
                    "grade" :int(parts[1])
                })
    except FileNotFoundError:
        pass            

def save_student(student_name,student_grade):
    with open("students.txt","a") as file:
        file.write(f"{student_name},{student_grade}\n")
    

def add_student():
    student_name = input("Enter Student Name:  ")
    if student_name =="":
        print("Please enter student name")
    else:
        try:
            student_grade = int(input("Enter grade: "))
            if student_grade < 0 or student_grade > 100:
                print("Grade must be between 0 and 100")
            else:
                students = {} 
                students["name"] = student_name
                students["grade"] = student_grade
                students_list.append(students)
                save_student(student_name,student_grade)
                print("Student added successfully")
        except ValueError:
            print("Please enter valid grade")        

def view_students():
    total = 0
    if(len(students_list) == 0):
        print("No student added yet!")
    else:
        for student in students_list:
            print(f"{student["name"]} - {student["grade"]}")
            total += student["grade"]
        average = round(total / len(students_list)) 
        print(f"Average grade : {average}")     

def find_topper():
    topper = max(students_list, key=lambda k: k["grade"])
    print(f"Top student: {topper["name"]} with {topper["grade"]}")

def menu():
    print("================================")
    print("Welcome to Student Grade Manager")
    print("================================")
    print("1. Add student")
    print("2. View all students")
    print("3. Find top student")
    print("4. Exit")

load_students()
isBrowersing  = True
while isBrowersing:
    menu()
    option = 0 # Default value
    try:
        option = int(input("Enter your option: ")) 
    except ValueError:
        print("Please enter valid option")
    if option == 1:
        add_student()
    elif option == 2:
        view_students()
    elif option == 3:
        find_topper()
    elif option == 4:
        print("Goodbye see you again!")
        isBrowersing = False        





    