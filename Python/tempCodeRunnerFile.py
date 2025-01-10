class Obj:
    "This is Obj class.It demonstrates the usage of special methods in Python."

    # This method is not a special method in Python. 
    # It seems like a typo and should be __str__ or __repr__ instead.
    def __name__(self):
        return "Object"

    # This method is a special method in Python, it's a static method that's automatically called when an object of the class is instantiated.
    # It's used to create a new instance of the class.
    def __new__(cls, *args, **kwargs):
        instance = super(Obj, cls).__new__(cls)
        print("instance is created")
        return instance

    # This method is a special method in Python, it's an instance method that's automatically called after the object is created.
    # It's used to initialize the attributes of the class.
    def __init__(self, value):
        self.value = value
        print("instance is initialized")

    # This method is a special method in Python, it's an instance method that's automatically called when the object is about to be destroyed.
    # It's used to release any system resources that the object is holding.
    def __del__(self):
        print("instance is destroyed")

    # This method is a normal instance method, it's used to display the value of the object.
    def show_value(self):
        print("Value:", self.value)

    # This method is a special method in Python, it's an instance method that returns a string representation of the object.
    # It's used to provide a human-readable representation of the object.
    def __str__(self):
        return "Obj with value " + str(self.value)

    def __repr__(self):
        return "Obj with value " + str(self.value)

# obje = Obj(42)
# obje.show_value()  # Value: 42

# obje.value = 100
# obje.show_value()  # Value: 100

# Accessing the __doc__ attribute
print(Obj.__doc__)

obj = Obj(10)  # Calls __new__ and then __init__

print(obj)     # Calls __str__

repr(obj)      # Calls __repr__

obj.show_value()  # Calls show_value

del obj 