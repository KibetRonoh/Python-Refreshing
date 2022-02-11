friend = "Kim"
user_name = input("enter Name: ")

if user_name == friend:
    print("hello, Friend")
else:
    print("Hello, Stranger")


################################
friends = ["jen", "kim", "anne"]
family = ["bob", "raph"]

name = input("enter name: ")

if name in friends:
    print("Hello, friend")
elif name in family:
    print("Hello, Family")
else:
    print("I dont know you")