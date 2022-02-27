# ARGUMENT Is the value you pass in to the function

# PARAMETER is a variable that accepts a value inside the function
"""car = {
    'make': 'ford',
    'model': 'fiesta',
    'mileage': 23000,
    'fuel_consumed': 400
}
"""
def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate['mileage'] / car_to_calculate['fuel_consumed']
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f'{name} does {mpg} miles per gallon')

calculate_mpg({
    'make': 'ford',
    'model': 'fiesta',
    'mileage': 23000,
    'fuel_consumed': 400
})