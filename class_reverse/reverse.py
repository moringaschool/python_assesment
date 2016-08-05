# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters

# Solution:
class InputOutString(object):
    # code goes here
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = raw_input("Write Down Any Word : ")

