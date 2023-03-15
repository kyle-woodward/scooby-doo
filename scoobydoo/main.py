from . import characters
import argparse

# here you can do more with pulling out class attributes and whatnot 
# but we are just going to use characters.Animals() for main()

# scooby = characters.Animals('scooby')
# print(f"Instance: {scooby}")
# print(f"gimme a catchphrase! :{scooby.gimme_a_catchphrase(scooby.name)}") # call a method that belongs to the parent class (Characters)

# shaggy = characters.People('shaggy','green','male')
# print(shaggy.kind) # global People attribute
# print(shaggy.shirtcolor) # local instance attributes defined upon instantiation
# print(shaggy.gender)

# redbeard = characters.Villains("Redbeard's ghost")
# print(redbeard)
# print(redbeard.kind)

def create_animal(char_name):
    char = characters.Animals(char_name)
    return char
def create_person(char_name):
    char = characters.People(char_name)
    return char
def create_villain(char_name):
    char = characters.Villains(char_name)
    return char

def main():
    # argparse to pass cli args
    parser = argparse.ArgumentParser(
    description="Gimme a catch phrase!",
    usage = "scoobydoo -n scooby -t animal"
    )
    
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        required=True,
        help="character name"
    )
    
    parser.add_argument(
        "-t",
        "--type",
        type=str,
        required=True,
        help = "character type"
    )
    
    
    #parse the args
    args = parser.parse_args()
    
    char_name = args.name
    char_type = args.type

    #call create_char()
    if char_type == "person":
        character = create_person(char_name)
    elif char_type == "animal":
        character = create_animal(char_name)
    elif char_type == "villain":
        character = create_villain(char_name)
    else:
        raise ValueError("invalid value given to -t --type")
    
    name = character.name
    
    print(character.gimme_a_catchphrase(name))
    
    return

if __name__ == "__main__":
    main()