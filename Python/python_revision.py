class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

student = Student("keval patel", 20)
student.display()  # Name: keval patel, Age: 20

a=10
b=20

a,b = b,a #

