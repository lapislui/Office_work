class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

class Dog(Animal):
    def speak(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching."

class Cat(Animal):
    def speak(self):
        return "Meow!"

    def scratch(self):
        return f"{self.name} is scratching."

class Bird(Animal):
    def speak(self):
        return "Chirp!"

    def fly(self):
        return f"{self.name} is flying."

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

print(dog.speak())
print(dog.eat())
print(dog.sleep())
print(dog.fetch())

print(cat.speak())
print(cat.eat())
print(cat.sleep())
print(cat.scratch())

print(bird.speak())
print(bird.eat())
print(bird.sleep())
print(bird.fly())