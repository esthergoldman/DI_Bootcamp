
# Step 1
# Create a new class called Animal.
# It should take 2 parameters, "species" and "habitat"
# (make the class defintion and the init method)

# Step2
# add another parameter to your class, which is the sound that the animal makes.
# write a method called talk, that prints out the animals sound.

# Step3
# create 2 instance of animals, and make each one talk.


class Animal:
    def __init__(self, species, habitat, sound):
        self.species = species
        self.habitat = habitat
        self.sound = sound

    def talk(self):
        print(self.species + self.sound)

    def lives(self):
        print(self.species + self.habitat)


a1 = Animal("cat ", "home", "miu")
a1.talk()
a1.lives()

a2 = Animal("dog ", "garden", "woff")
a2.talk()
a2.lives()
