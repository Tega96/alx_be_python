"""
Docstring for alx_be_python.control-flow.pattern_drawing

Develop a Python script named pattern_drawing.py. 
This script will prompt the user to enter a positive integer, 
then use nested loops to print a square pattern of that size made of asterisks (*).
"""

pattern_size = int(input("Enter the size of the pattern: "))
i = 0
while i < pattern_size:
    for pattern in range(1, pattern_size + 1):
        print("*", end="")
    print()
    i += 1