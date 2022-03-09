
"""
implement __init__( name , type , tricks, noise):
implement the following methods:
sleep() - increases the pets energy by 25
eat() - increases the pet's energy by 5 & health by 10
play() - increases the pet's health by 5
noise() - prints out the pet's sound
"""


class Pet:
    def __init__(self, name, types, tricks, age):
        self.name = name
        self.type = types
        self.tricks = tricks
        self.age = age
        self.health = 100
        self.energy = 70

    def sleep(self):
        self.energy += 25
        return self

    def eat(self, energy, health):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        return 'Bark!'

#subclass
class Husky(Pet): 
    def __init__(self, name, types, tricks, age):
        super().__init__(name, types, tricks, age)
    
    def fetch_ability(self):
        if self.age < 2: 
            return 8
        elif self.age < 10:
            return 10 
        else: 
            return 7 

    def noise(self):
        return 'Woof!'

class Poodle(Pet):
    def __init__(self, name, types, tricks, age):
        super().__init__(name, types, tricks, age)
    
    def noise(self):
        return 'Arooo!'


buddy = Husky("Buddy", "husky", "roll-over", 8)
print(buddy.name, buddy.type, buddy.tricks, buddy.noise(), buddy.fetch_ability())
