import os
import sys
import csv

class Student:

    def __init__(self,student_no, firstname, lastname, classroom, grade=None):
        self.student_no = student_no
        self.firstname = firstname
        self.lastname = lastname
        self.classroom = classroom
        self.grade = grade if grade else "N/A"


    def __str__(self):
        return f"NO: {self.student_no} | {self.firstname} {self.lastname} | {self.classroom} | Grade : {self.grade} "

    def to_dict(self):
        return {
            'student_no' : self.student_no,
            'firstname' : self.firstname,
            'lastname' : self.lastname,
            'classroom': self.classroom,
            'grade' : self.grade
        }

class StudentRegister:
    
    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.students = {}
        self.load_from_file()

    def add(self,student):
        self.students[student.student_no] = student
    
    def remove (self,student_no):
        if student_no in self.students:
            del self.students[student_no]
            return True
        else :
            return False
    
    def search (self, student_no):
        return self.students.get(student_no)
    
    def list_all(self):
        return list(self.students.values())
    
    def save_to_file(self):
        with open(self.filename, 'w', newline='', encoding='utf-8')as file :
            if self.students:
                fieldnames = ['student_no', 'firstname', 'lastname', 'classroom', 'grade'] 
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for student in self.students.values():
                    writer.writerow(student.to_dict())

    def load_from_file(self):
        
        if os.path.exists(self.filename):
            with open (self.filename, 'r', encoding='utf-8' ) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        row['student_no'],
                        row['firstname'],
                        row['lastname'],
                        row['classroom'],
                        row['grade']
                    )

                    self.students[student.student_no]= student



def main():

    register = StudentRegister()


    while True:
        print("\n" + "="*50)
        print("STUDENT REGISTER SYSTEM".center(50))
        print("="*50)
        print("1. Add new student")
        print("2. Delete a student")
        print("3. Search a student")
        print("4. List all students")
        print("5. Save and exit")
        print("="*50)

        choice = input("Your choice (1-5): ").strip()

        if choice == "1":
            add_student(register)
        elif choice =="2":
            remove_student(register)
        elif choice =="3":
            search_student(register)
        elif choice =="4":
            list_all_students(register)
        elif choice =="5":
            register.save_to_file()
            print("\n Everything is saved succesfully! Goodbye!")
            sys.exit(0)
        else:
            print("\n INVALID CHOICE!!! PLEASE ENTER 1, 2, 3, 4 or 5 !")

def add_student(register):
    print("\n--- ADD NEW STUDENT ---")

    student_no= input("Student No.: ").strip()
    if not student_no:
        print("Student No. cannot be empty!")
        return
    
    if register.search(student_no):
        print(f"{student_no} is already registered to system!")
        return
    
    firstname = input("First Name: ").strip()
    lastname = input("Last Name: ").strip()
    classroom = input("Classroom: ").strip()
    grade = input("Grade (optional): ").strip()

    if not firstname or not lastname or not classroom:
        print("You must enter First and Last name or classroom name correctly!")
        return
    
    student = Student(student_no, firstname, lastname, classroom, grade if grade else "N/A")
    register.add(student)
    register.save_to_file()
    print (f"\n {firstname} {lastname} added succesfully!")

def remove_student(register):
    print("\n--- REMOVE STUDENT ---")
    
    student_no = input("Number of the student that you want to remove: ").strip()
    
    student = register.search(student_no)
    if student:
        confirm = input(f"{student.firstname} {student.lastname} is going to be removed. Are you sure? (y/n): ").lower()
        if confirm == 'y':
            register.remove(student_no)
            register.save_to_file()
            print("Student removed successfully!")
        else:
            print("Process aborted")
    else:
        print(f"We couldn't find any student that has number {student_no} .")


def search_student(register):
    print("\n--- SEARCH STUDENT ---")
    
    student_no = input("Student No: ").strip()
    student = register.search(student_no)
    
    if student:
        print("\n" + "-"*50)
        print(student)
        print("-"*50)
    else:
        print(f"We couldn't find any student that has number {student_no} .")


def list_all_students(register):
    print("\n--- ALL STUDENTS ---")
    
    students = register.list_all()
    
    if not students:
        print("There are no students.")
        return
    
    print(f"\n Number of all registered students : {len(students)}")
    print("-"*50)
    for student in students:
        print(student)
    print("-"*50)


if __name__ == "__main__":
    main()
