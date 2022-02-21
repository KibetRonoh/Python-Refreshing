# consider the following source code.

class Developer(object):
    def __init__(self, skills):
        self.skills = skills

    def __add__(self, other):
        skills = self.skills + other.skills
        return Developer(skills)

    def __str__(self):
        return 'skills'

A = Developer('NodeJS')
B = Developer('Python')

#which functions are called when print( A + B) is executed