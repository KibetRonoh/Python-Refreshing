# AND give syou the first value if it is False, otherwise it gives you the second value
x = 35 and 0
print(x)


# OR gives you the first value if it is True, otherwise it gives you the second value
x = 0 or 35
print(x)

name = ""
surname = "Ronoh"

greeting = name or f"Mr. {surname}"
print(greeting)