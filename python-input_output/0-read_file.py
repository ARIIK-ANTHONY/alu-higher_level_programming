"""
This module provides a function to read a UTF-8 text file and print its contents.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The path to the text file (default is an empty string).

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())
