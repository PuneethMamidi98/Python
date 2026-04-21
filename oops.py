class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"{self.name} - {self.grade}")


class StudentManager:
    def __init__(self):
        self.student_list = []

    def add_student(self):
        name = input("Enter Student Name: ")
        if name == "":
            print("Please enter student name!")
            return
        try:
            grade = int(input("Enter Student Grade: "))
            if grade < 0 or grade > 100:
                print("Grade should in betwwen 1 to 100")
                return
            student = Student(name,grade)
            self.student_list.append(student)
            self.save_student(name,grade)
            print("Student added succcesfully")
        except ValueError:
            print("Please enter valid grade!")

    def view_students(self):
        total = 0
        if len(self.student_list) == 0:
            print("No student added yet")
        else:
            for student in self.student_list:
                student.display()
                total += student.grade
            average = round(total / len(self.student_list)) 
            print(f"Average grade : {average}")
    def find_topper(self):
        if len(self.student_list) == 0:
            print("No students added yet!")
            return
        topper = max(self.student_list, key=lambda s: s.grade)
        print(f"Top student: {topper.name} with {topper.grade}")

    def load_students(self):
        try:
            with open("students.txt","r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    student = Student(parts[0],int(parts[1]))
                    self.student_list.append(student)
        except FileNotFoundError:
            pass

    def save_student(self,name,grade):
        with open("students.txt","a") as file:
            file.write(f"{name},{grade}\n")
    def menu(self):
        print("================================")
        print("Welcome to Student Grade Manager")
        print("================================")
        print("1. Add student")
        print("2. View all students")
        print("3. Find top student")
        print("4. Exit")

manager = StudentManager()        

manager.load_students()
isBrowersing = True
while isBrowersing == True:
    manager.menu()
    option = 0
    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Enter valid option number")

    if option == 1:
        manager.add_student()
    elif option == 2:
        manager.view_students()
    elif option == 3:
        manager.find_topper()
    elif option == 4:
        print("Goodbye see you again!")
        isBrowersing = False                                                           





                



                  



        
       
      
       

        

        