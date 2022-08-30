'''
2. Create a module called main.py that imports greet() from greeter.py
and calls the function with the argument "Real Python" .
'''
import greeter
from package_exercises import string
from package_exercises import math

greeter.greet("Real Python")
length = 5
width = 8
print(string.shout(f'the area of a {length}-by-{width} rectangle is {math.area(length, width)}'))