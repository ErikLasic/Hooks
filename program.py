# pylint: disable=missing-function-docstring
"""
This is a module-level docstring that describes the purpose of the neke module.
"""

def greet(name):
    """This function greets the person passed in as a parameter."""
    print("Hello, " + name + ". How are you doing?")

def calculate_area(length, width):
    """This function calculates the area of a rectangle."""
    area = length * width
    return area

greet("John")
# Output: Hello, John. How are you doing?

area = calculate_area(5, 3)
print("The area of the rectangle is", area)
# Output: The area of the rectangle is 15
