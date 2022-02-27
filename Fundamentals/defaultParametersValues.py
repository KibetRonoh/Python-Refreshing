"""def add(x , y):
    total = x + y
    return total
print(add(5, 10))"""

def add(x , y=3): # default parameters # we are doing this when we are defining the function
    total = x + y
    return total
print(add(x=5, y=10))# running it when calling a function
# they are called named arguments/ ketword args 


"""def add(x , y=5):
    total = x + y
    return total
print(add(x=5, 10))""" # wrong,

# highly discouraged to use variable as default values

print(1, 2, 3, 4, 5,6 ,7 ,8, sep='---')