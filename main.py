from scoobydoo import animals

# initizialize custom instance of animals class
scrappy = animals("scrappy",["Puppy-Power!","Lemme at em!"])

# apply a method belonging to that class
phrase = scrappy.gimme_a_catchphrase("scrappy")
print(phrase)