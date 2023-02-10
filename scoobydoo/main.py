import characters

scooby = characters.Animals('scooby','dog')
print(f"Instance: {scooby}")
print(f"kind: {scooby.kind}") # global Animals attribute
print(f"species: {scooby.species}") # local instance attributes defined upon instantiation
print(f"gimme a catchphrase! :{scooby.gimme_a_catchphrase(scooby.name)}") # call a method that belongs to the parent class (Characters)

# shaggy = characters.People('shaggy','green','male')
# print(shaggy.kind) # global People attribute
# print(shaggy.shirtcolor) # local instance attributes defined upon instantiation
# print(shaggy.gender)

# redbeard = characters.Villains("Redbeard's ghost")
# print(redbeard)
# print(redbeard.kind)