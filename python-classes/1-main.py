#!/usr/bin/python3
"""
Test script for the Square class.
"""

Square = __import__('1-square').Square

# Create a square with size 3
my_square = Square(3)

# Print the object type and its internal attribute
print(type(my_square))  # <class '1-square.Square'>
print(my_square.__dict__)  # Shows {'_Square__size': 3}

# Access attempts to private attributes
try:
    print(my_square.size)  # Raises AttributeError
except Exception as e:
    print(e)

try:
    print(my_square.__size)  # Raises AttributeError
except Exception as e:
    print(e)
