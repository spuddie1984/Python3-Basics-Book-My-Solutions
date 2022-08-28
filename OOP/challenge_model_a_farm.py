'''
Before you write any code, grab a pen and paper and sketch out a
model of your farm, identifying classes, attributes, and methods.
Think about inheritance. How can you prevent code duplication?
Take the time to work through as many iterations as you feel are
necessary.

The actual requirements are open to interpretation, but try to adhere
to these guidelines:
1. You should have at least four classes: the parent Animal class and
at least three child animal classes that inherit from Animal .
2. Each class should have a few attributes and at least one method
that models some behavior appropriate for a specific animal or all
animals—walking, running, eating, sleeping, and so on.
3. Keep it simple. Utilize inheritance. Make sure you output details
about the animals and their behaviors.

'''

class Animal(object):
    def __init__(self,name, feet_type):
        self.name = name
        self.feet_type = feet_type

    def __str__(self):
        return f"I'm {self.name} and I have {self.feet_type}s!"

    def speak(self, sound):
        return f'{self.name} says {sound}'

    def sleep(self, where):
        return f'{self.name} likes to sleep in the {where}'

class Dog(Animal):
    def speak(sound="Woof"):
        return super().speak(sound)

    def sleep(self,where="Kennel"):
        return super().sleep(where)

class Pig(Animal):
    def speak(self,sound="Oink"):
        return super().speak(sound)

    def sleep(self,where="Barn"):
        return super().sleep(where)

class Sheep(Animal):
    def speak(self,sound="Bleat"):
        return super().speak(sound)

    def sleep(self,where="Paddock"):
        return super().sleep(where)

joey = Dog('Joey','Paw')
peppy = Pig('Peppy','Hoof')
bashful = Sheep('Bashful','Hoof')
print(joey.sleep())
print(joey)
