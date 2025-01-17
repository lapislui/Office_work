# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
first_element = my_list[0]  # Access first element
last_element = my_list[-1]  # Access last element

# Modifying elements
my_list[0] = 10  # Change first element to 10

# Adding elements
my_list.append(6)  # Add 6 to the end of the list
my_list.insert(2, 15)  # Insert 15 at index 2

# Removing elements
my_list.remove(3)  # Remove first occurrence of 3
popped_element = my_list.pop()  # Remove and return the last element
popped_index_element = my_list.pop(1)  # Remove and return element at index 1

# Slicing a list
sub_list = my_list[1:3]  # Get elements from index 1 to 2

# List length
list_length = len(my_list)  # Get the number of elements in the list

# List concatenation
another_list = [7, 8, 9]
combined_list = my_list + another_list  # Combine two lists

# List repetition
repeated_list = my_list * 2  # Repeat the list twice

# Checking for existence
is_in_list = 10 in my_list  # Check if 10 is in the list

# Iterating through a list
for element in my_list:
    print(element)  # Print each element in the list

# List comprehension
squared_list = [x**2 for x in my_list]  # Create a new list with squares of elements

# Sorting a list
sorted_list = sorted(my_list)  # Return a new sorted list
my_list.sort()  # Sort the list in place

# Reversing a list
reversed_list = my_list[::-1]  # Return a new list that is reversed
my_list.reverse()  # Reverse the list in place
# Extending a list
my_list.extend([11, 12, 13])  # Add multiple elements to the end of the list

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)  # Add a single element
my_set.update([7, 8, 9])  # Add multiple elements

# Removing elements
my_set.remove(3)  # Remove an element, raises KeyError if not found
my_set.discard(4)  # Remove an element, does nothing if not found
popped_element = my_set.pop()  # Remove and return an arbitrary element

# Checking for existence
is_in_set = 5 in my_set  # Check if 5 is in the set

# Set operations
another_set = {4, 5, 6, 7}
union_set = my_set | another_set  # Union of two sets
intersection_set = my_set & another_set  # Intersection of two sets
difference_set = my_set - another_set  # Difference of two sets
symmetric_difference_set = my_set ^ another_set  # Symmetric difference of two sets

# Iterating through a set
for element in my_set:
    print(element)  # Print each element in the set

# Set comprehension
squared_set = {x**2 for x in my_set}  # Create a new set with squares of elements

# Set length
set_length = len(my_set)  # Get the number of elements in the set

# Clearing a set
my_set.clear()  # Remove all elements from the set

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
first_element = my_tuple[0]  # Access first element
last_element = my_tuple[-1]  # Access last element

# Slicing a tuple
sub_tuple = my_tuple[1:3]  # Get elements from index 1 to 2

# Tuple length
tuple_length = len(my_tuple)  # Get the number of elements in the tuple

# Tuple concatenation
another_tuple = (6, 7, 8)
combined_tuple = my_tuple + another_tuple  # Combine two tuples

# Tuple repetition
repeated_tuple = my_tuple * 2  # Repeat the tuple twice

# Checking for existence
is_in_tuple = 3 in my_tuple  # Check if 3 is in the tuple

# Iterating through a tuple
for element in my_tuple:
    print(element)  # Print each element in the tuple

# Tuple comprehension (using a generator expression)
squared_tuple = tuple(x**2 for x in my_tuple)  # Create a new tuple with squares of elements

# Converting a list to a tuple
my_list = [1, 2, 3]
converted_tuple = tuple(my_list)  # Convert list to tuple

# Unpacking a tuple
a, b, c, d, e = my_tuple  # Unpack elements of the tuple into variables

# Finding the index of an element
index_of_element = my_tuple.index(3)  # Find the index of the first occurrence of 3

# Counting occurrences of an element
count_of_element = my_tuple.count(2)  # Count the number of occurrences of 2