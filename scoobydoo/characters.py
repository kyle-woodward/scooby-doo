import random
from .catchphrases import phrases
# parent class
class Character:
    def __init__(self,name):
        self.name=name
    
    def gimme_a_catchphrase(self,name):
        kind = self.kind
        options = phrases[kind][name]
        #print(kind_opts)
        return random.choice(options)
        

# define child classes of Character
class People(Character):
    kind = 'person' # class variable shared by all instances
    def __init__(self, name, shirtcolor,gender):
        super().__init__(name)  # inherits Character class attributes
        self.shirtcolor = shirtcolor # unique attributes to the People sub-class
        self.gender = gender
   
class Animals(Character):
    kind='animal'
    def __init__(self, name): # can pass more args to init that can be defined as an attribute via self.attribute = attribute
        super().__init__(name)
        #self.species = species

class Villains(Character):
    kind='villain'
    def __init__(self,name,unmasked=False):
        super().__init__(name)
        self.unmasked=unmasked
    # how to deal with unmasked bool?
    # gimme_a_catchphrase() is parent method so the attribute unmasked wouldn't be in scope at Characters
    # def unmasked_phrase(unmasked):
    #     if unmasked:
    #         return "I would have gotten away with it too, if it weren't for those meddling kids!"
    #     else: