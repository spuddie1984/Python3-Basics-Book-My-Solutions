'''
1. Create a GoldenRetriever class that inherits from the Dog class. Give
the sound argument of GoldenRetriever.speak() a default value of
"Bark" . Use the following code for your parent Dog class:
class Dog:
species = "Canis familiaris"
def __init__(self, name, age):
self.name = name
self.age = age
def __str__(self):
return f"{self.name} is {self.age} years old"
def speak(self, sound):
return f"{self.name} says {sound}"
'''

from turtle import window_width


class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    
    def speak(self, sound="Bark"):
        return super().speak(sound)

joey = GoldenRetriever('Joey',10)
joey.speak()

'''
2. Write a Rectangle class that must be instantiated with two at-
tributes: .length and .width . Add an .area() method to the class
that returns the area ( length * width ) of the rectangle.
Then write a Square class that inherits from the Rectangle class and
is instantiated with a single attribute called .side_length . Test
your Square class by instantiating a Square with a .side_length of 4 .
Calling .area() should return 16 . Set the .width property of your
Square instance to 5. Then call .area() again. The return value should be 20 .

This example illustrates how class inheritance isn’t always a
good model for subset relationships. In mathematics, all squares
are rectangles, but this isn’t necessarily true in computer pro-
gramming.
Be careful to define behaviors so that they reflect expectations,
and use class hierarchies with caution.
'''

class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Square(Rectangle):
    def __init__(self, side_length):
        return super().__init__(side_length, side_length)

square = Square(5)
square.width = 4

print(square.area())