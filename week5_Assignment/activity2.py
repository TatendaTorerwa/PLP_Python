class Animal:
    def move(self):
        print("This animal moves.")

class Bird(Animal):
    def move(self):
        print("Flying in the sky! 🦅")

class Fish(Animal):
    def move(self):
        print("Swimming in the water! 🐟")

class Dog(Animal):
    def move(self):
        print("Running on the ground! 🐕")

# Example usage
animals = [Bird(), Fish(), Dog()]

for animal in animals:
    animal.move()
