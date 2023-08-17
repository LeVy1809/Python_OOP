class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def  add_course(self, course):
        self.courses.append(course)

    def display_info(self):
        print('Name:', self.name)
        print('Student ID:', self.student_id)
        print('Courses:', ', '.join(self.courses))

student = Student('Le Vy', '22521702')

student.add_course('Object-Oriented Programming')
student.add_course('Data Structures and Algorithms')
student.add_course('E-commerce')

student.display_info()