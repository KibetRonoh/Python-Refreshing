class Movie:
    def __init__(self, name, director,  year):
        self.name = name # self.name is not a variable but its a property of self
        self.year = year
        self.director = director

matrix = Movie("The Matrix", "Patoski", 1990)

print(matrix.name)
print(matrix.director)