
"""
implement __init__( first_name , last_name , treats , pet_food , pet )

implement the following methods:
walk() - walks the ninja's pet invoking the pet play() method
feed() - feeds the ninja's pet invoking the pet eat() method
bathe() - cleans the ninja's pet invoking the pet noise() method
"""

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self


"""
implement __init__( name , type , tricks, noise):
implement the following methods:
sleep() - increases the pets energy by 25
eat() - increases the pet's energy by 5 & health by 10
play() - increases the pet's health by 5
noise() - prints out the pet's sound
"""



mav = Ninja("Maverick", "Sison", "Husky", "cookies", "chicken")
print(mav.first_name, mav.last_name, mav.pet, mav.treats, mav.pet_food)







