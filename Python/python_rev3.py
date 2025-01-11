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

