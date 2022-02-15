# EXAMPLE
numbers = [0, 1, 2, 3, 4, 5]
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)

print(doubled_numbers)

# LIST COMPREHENSION 1
numbers = [0, 1, 2, 3, 4, 5]
doubled_numbers = [number * 2 for number in numbers]

print(doubled_numbers)


# LIST COMPREHENSION 2
doubled_numbers = [number * 2 for number in range(6)]

print(doubled_numbers)


# LIST COMPREHENSION 3
friend_ages = [22, 34, 19, 56, 37]
age_strings = [f'my friend is {age} years old.' for age in friend_ages]

print(age_strings)


# LIST COMPREHENSION 4
names = ["Rolf", "Kibet", "Jen"]
lower = [name.lower() for name in names]

print(lower)



# LIST COMPREHENSION 5
friend = input("Enter your friends name: ")
friends = ["Rolf", "Kibet", "Jen"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    print(f"{friend} is one of your friends")

if friend.lower() in friends_lower:
    friend_titlecased = friend.title()
    print(f"{friend_titlecased} is one of your friends")


# LIST COMPREHENSION 6
friend = input("Enter your friends name: ")
friends = ["Rolf", "Kibet", "Jen"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    friend_titlecased = friend.title()
    print(f"{friend_titlecased} is one of your friends")



# LIST COMPREHENSION 8
friends = ['Rolf', 'ruth', 'charlie', 'jen']
guests = ['jose', 'Bob', 'Rolf', 'Charlie', 'michael']


present_friends = [
    name.title() # new thing that you want to put into your list
    for name in guests # iteration over an existing iterable
    if name.lower()in [f.lower() for f in friends] # list comprehension
]
