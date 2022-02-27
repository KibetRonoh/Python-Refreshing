class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks)/ len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
    
    def weekly_salary(self):
        return self.salary * 37.5

kibet = WorkingStudent("Kibet", "Moi", 2000)
print(kibet.salary)
kibet.marks.append(79)
kibet.marks.append(98)
print(kibet.average())
print(kibet.weekly_salary())

