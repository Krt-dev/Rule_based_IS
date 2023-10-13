
def identify_pokemon_type():
    type = input("What is the type of the starter Pokémon? ").lower()
    if type == "electric":
       return electric_pokemon_yellow()
    elif type == "fire":
        return fire_pokemon_red()
    elif type == "grass":
        return grass_pokemon_green()
    elif type == "water":
        return water_pokemon_blue()
    else:
        print("Its not a starter Pokemon type")


def electric_pokemon_yellow():
    specie = input("does the Pokemon resemble a mouse?").lower()
    if specie == "yes":
        return "Pikachu"
    else:
        return "not a starter Pokemon"
    

def fire_pokemon_red():
    color = input("Does the color of the Pokemon contain Red?")
    if color == "yes":
        specie = input("what real world animal does the Pokemon look like?").lower()
        if specie == "lizard":
         return "Charmander"
        elif specie == "fox":
            return "Fennekin"
        elif specie == "cat":
            return "Litten"
        elif specie == "crocodile":
            return "Fuecoco"
        elif specie == "mouse":
            return "Cyndaquil"
        elif specie == "chicken":
            return "Torchic"
        elif specie == "monkey":
            return "Chimchar"
        elif specie == "pig":
            return "Tepig"
        elif specie == "rabbit":
            return "Scorbunny"
        else:
            return "not a starter"
    else:
        return "not a fire type"
    

def grass_pokemon_green():
    color = input("Does the color of the Pokemon contain Green?")
    if color == "yes":
        specie = input("what real world animal does the Pokemon look like?").lower()
        if specie == "turtle":
            return "Bulbasaur"
        elif specie == "mole":
            return "Chespin"
        elif specie == "owl":
            return "Rowlett"
        elif specie == "cat":
            return "Sprigatito"
        elif specie == "dinosaur":
            return "Chikorita"
        elif specie == "gecko":
            return "Treecko"
        elif specie == "tortoise":
            return "Turtwig"
        elif specie == "Snake":
            return "Snivy"
        elif specie == "tarsier":
            return "Grookey"
        else:
            return "not a starter"
    else:
        return "not a grass type"

def water_pokemon_blue():
    color = input("Does the color of the Pokemon contain Blue?")
    if color == "yes":
        specie = input("what real world animal does the Pokemon look like?").lower()
        if specie == "tortoise":
            return "Squirtle"
        elif specie == "frog":
            return "Froakie"
        elif specie == "seal":
            return "Popplio"
        elif specie == "duck":
            return "Quaxly"
        elif specie == "crocodile":
            return "totodile"
        elif specie == "axolotl":
            return "Mudkip"
        elif specie == "penguin":
            return "Piplup"
        elif specie == "otter":
            return "Oshawott"
        elif specie == "salamander":
            return "sobble"
        else:
            return "not a starter"
    else:
        return "not a water type"

# Main program
if __name__ == "__main__":
        print("-------------Welcome to the Starter Pokémon Identification---------------")
        pokemon_name = identify_pokemon_type()
        print("The Pokémon you're describing is", pokemon_name)
