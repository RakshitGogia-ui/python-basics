name = input("enter your name")
age = int(input("enter your age"))

if age >=18:
    print(name,'is an adult')
else:
    print(name,'is a minor')

for i in range(1,6):
    print("number", i)

def greet(user):
    print("hello", user)

greet(name)    
