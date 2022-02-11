# For loop is used to repeat something for defined number of times
elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index in elements:
    print(index)

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Kim", "grade": 54},
    {"name": "pato", "grade": 89},
    {"name": "geff", "grade": 97}
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}")
