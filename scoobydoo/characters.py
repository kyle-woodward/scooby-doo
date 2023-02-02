import random

class people:
    kind = 'human'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

shaggy = people('shaggy')
    
class animals:
    kind = 'dog'

    def __init__(self,name:str,phrases:list):
        self.phrases = {name:phrases}

    def gimme_a_catchphrase(self,n):
        phrase_list = self.phrases[n]
        return random.choice(phrase_list)
