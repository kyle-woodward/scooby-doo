import random

class Character:
    def __init__(self,name):
        self.name=name
    
    def gimme_a_catchphrase(self,n):
        phrase_list = self.phrases[n]
        return random.choice(phrase_list)

# define child class of Character
class People(Character):
    kind = 'human'         # class variable shared by all instances

    def __init__(self, name, shirtcolor,gender):
        super(Character, self).__init__(name)    # instance variable unique to each instance
        self.shirtcolor = shirtcolor
        self.gender = gender

shaggy = People('shaggy')
    
class Animals(Character):
    def __init__(self, name, species):
        super(Character, self).__init__(name)    # instance variable unique to each instance
        self.species = species

class Villains(Character):
    def __init__(self,name,unmasked=False):
        super(Character, self).__init__(name)