from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('Woof!')

class Cat(Animal):
    def make_sound(self):
        print('Meow!')

class Monkey(Animal):
    def make_sound(self):
        print('Ooh ooh aah aah!')

animals = [Dog(),Cat(),Monkey()]
for animal in animals:
    animal.make_sound()