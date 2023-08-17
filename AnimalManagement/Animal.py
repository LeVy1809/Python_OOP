class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        print('\nName:', self.name)
        print('Species:', self.species)
        print('Age:', self.age)    

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('Woof!')

class Cat(Animal):
    def make_sound(self):
        print('Meow!')

dog = Dog('Lucy', 'dog', 5)
dog.display_info()
dog.make_sound()

cat = Cat('Mimi', 'cat', 2)
cat.display_info()
cat.make_sound()