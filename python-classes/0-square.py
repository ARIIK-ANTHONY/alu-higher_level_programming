#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))  # Prints the type of the object
print(my_square.__dict__)  # Prints the dictionary of attributes (should be empty)
