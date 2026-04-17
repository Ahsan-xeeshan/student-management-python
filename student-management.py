# =============== Student Database ==================

class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls,student):
        for s in cls.student_list:
          if s.student_id == student.student_id:
            print("Student ID already exists!")
            return
        cls.student_list.append(student)
    
    @classmethod
    def view_all_students(cls):
        if not cls.student_list:
            print('No students found')
        else:
            for student in cls.student_list:
                student.view_student_info()

    @classmethod
    def find_student(cls,student_id):
        for student  in cls.student_list:
            if student.student_id == student_id:
                return student
        return None


# =============== Student Info ==================

class Student:
    def __init__(self,student_id,name, department,is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled


    @property
    def student_id(self):
        return self.__student_id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def department(self):
        return self.__department
    
    @property
    def is_enrolled(self):
        return self.__is_enrolled

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f'{self.__name} is now enrolled')
        else:
            print(f'{self.__name} is already enrolled')
    
    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f'{self.__name} is now dropped out')
        else:
            print(f'{self.__name} is already dropped out')
    
    def view_student_info(self):
         status = 'Enrolled' if self.__is_enrolled else 'Not Enrolled'         
         print(f"🆔 ID         : {self.__student_id}")
         print(f"👤 Name       : {self.__name}")
         print(f"🏫 Department : {self.__department}")
         print(f"📌 Status     : {status}")
         print("=" * 45)
        
    
    def __repr__(self):
        return (f"Student(ID={self.__student_id}, "
                f"Name={self.__name}, "
                f"Dept={self.__department}, "
                f"Enrolled={self.__is_enrolled})")
    

s1 = Student(101, "Nazmul Ahsan", "CSE", True)
s2 = Student(102, "Ashim Chowdhury", "EEE", False)
s3 = Student(103, "Redowan Karim", "BBA", False)



# =============== Helper Functions ==================


def get_student(action):
    try:
        s_id = int(input(f'Enter Student ID to {action}: '))
        student = StudentDatabase.find_student(s_id)
        if student:
            return student
        else:
            print(f"Student ID {s_id} not found!")
            return None
    except ValueError:
        print('Please enter a valid numeric ID!')
        return None


# =============== Sample Data ==================

StudentDatabase.add_student(s1)
StudentDatabase.add_student(s2)
StudentDatabase.add_student(s3)


# =============== Menu System ==================

while True:
    print("\n" + "=" * 45)
    print(" Student Management System ")
    print("=" * 45)
        
    print('1. View All Students')
    print('2. Enroll Student')
    print('3. Drop Student')
    print('4. Exit')
    choice = input('Enter your choice (1-4): ')

    if choice == '1':
        print("\n" + "=" * 45)
        print("         STUDENT INFORMATION")
        print("=" * 45)
        StudentDatabase.view_all_students()
    
    elif choice == '2':
        student = get_student("enroll")
        if student:
            student.enroll_student()
    
    elif choice == '3':
        student = get_student("drop")
        if student:
                student.drop_student()         

    elif choice == '4':
        print('Exiting program...')
        break
    
    else:
        print('Invalid choice. Try again')
