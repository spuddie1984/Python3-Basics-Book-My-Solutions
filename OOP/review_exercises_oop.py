'''
1. Modify the Dog class to include a third instance attribute called
coat_color , which stores the color of the dog’s coat as a string.
Store your new class in a file and test it out by adding the following
code at the bottom of the code:
philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}.")
The output of your program should be the following:
Philo's coat is brown.
'''

class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


philo = Dog("Philo", 5, "brown")

print(f"{philo.name}'s coat is {philo.coat_color}.")

'''
2. Create a Car class with two instance attributes: .color , which stores
the name of the car’s color as a string, and .mileage , which stores
the number of miles on the car as an integer. Then instantiate
two Car objects—a blue car with 20,000 miles and a red car with
30,000 miles—and print out their colors and mileage. Your output
should look like this:
The blue car has 20,000 miles.
The red car has 30,000 miles.

3. Modify the Car class with an instance method called .drive() ,
which takes a number as an argument and adds that number to
the .mileage attribute. Test that your solution works by instantiat-
ing a car with 0 miles, then call .drive(100) and print the .mileage
attribute to check that it is set to 100 .

'''

class Car(object):

    def __init__(self, color, mileage):
        self.color = color 
        self.mileage = mileage
    
    def drive(self,add_miles):
        self.mileage += add_miles

red_car = Car('blue', 20_000)
blue_car = Car('red', 30_000)
blue_car.drive(100)

for car in (red_car,blue_car):
    print(f'The {car.color} car has {car.mileage:,} miles.')
