def greet():
    print('Hello kib')

greet()

########################################
def greet():
    print('HELLO HILL')
hello = greet

hello()

########################################
"""def average(seq):
    return sum(seq) / len(seq)

avg = lambda seq: sum(seq) / len(seq)
"""

avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

operations = {
    "average": avg,
    "total": total,
    "top":top
}

students = [
    {'name': 'Rolf', 'grades': (67, 78, 98, 100)},
    {'name': 'Kim', 'grades': (61, 68, 90, 90)},
    {'name': 'Kib', 'grades': (67, 72, 89, 100)},
    {'name': 'Pato', 'grades': (50, 70, 98, 100)},
    
]

for student in students:
    name = student['name']
    grades = student['grades']

    print(f'Student: {name}')
    operation = input("Enter 'average', 'total', or 'top'")

    if operation =='average':
        print(avg(grades))
    elif operation == 'total':
        print(total(grades))
    elif operation == 'top':
        print(top(grades))

###########################################
###########################################
# we use dictionary to create associations in python
###########################################
###########################################

operation_function = operations[operation]
print(operation_function(grades))