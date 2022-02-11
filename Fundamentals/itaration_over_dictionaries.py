friends_ages = {"Rolf": 21, "anne": 34, "Bob": 19}

for name in friends_ages:
    print(name) # Itarating over dictionaries keys

##########################################
for age in friends_ages.values():
    print(age)


#############################################

for name, age in friends_ages.items(): #Destructuring
    print(f"{name} is {age} years old.")


