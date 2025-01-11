# Example of a for loop in Python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
    
    # Example of iterating over a string in Python using next
    my_string = "Hello, World!"
    string_iterator = iter(my_string)

    while True:
        try:
            char = next(string_iterator)
            print(char)
        except StopIteration:
            break
        
        
# Example of iterating over a list in Python using next
mylist = [1, 2, 3, 4, 5]
list_iterator = iter(mylist)

while True:
    try:
        item = next(list_iterator)
        print(item)
    except StopIteration:
        break

for x in mylist:
    print(x)


class myclass:
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.x:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration
    
nums= myclass(5)
myiter = iter(nums)
while True:
    try:
        print(next(myiter))
    except StopIteration:
        break
