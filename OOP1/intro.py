my_student = {
    "name": 'Kib Ronoh',
    "grades": [67, 98, 89, 100, 79]

}
"""
def average_grades(student):
    return sum(student['grades']) / len(student['grades'])

print(average_grades(my_student))"""


# Class is something tha defines what the objects are

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)
#create an oblect called student_one
# and we create an new object in python by calling its class
student_one = Student( 'Rolf Kibet', [90, 80, 99, 79, 100])

print(student_one.grades)
print(student_one.average())
print(Student.average(student_one))