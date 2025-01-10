class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name, "Age:", self.age)

student = Student("keval patel", 20)
student.display()  # Name: keval patel, Age: 20

a=10
b=20

print("Before swap: a =", a, "b =", b)
a, b = b, a  # tuple packing and unpacking
print("After swap: a =", a, "b =", b)


class NewClass:
    def __init__(self, x):
        self.x = x

    def func(self):
        print("x =", self.x)

obj = NewClass(10)
obj.func()  # x = 10 

print("obj.x= ",obj.x)

class Welcome:
    def __init__(self, message):
        self.message = message

    def welcome_func(self):
        print(self.message)

welcome_obj = Welcome("Welcome to the Python programming world!")
welcome_obj.welcome_func()  # Welcome to the Python programming world!