import random
count = 2



all_fighters = ("Random", "Mario", "Donkey Kong", "Link", "Samus", "Dark Samus", "Yoshi", "Kirby", "Fox", "Pikachu", "Luigi", "Ness", "Captain Falcon", "Jigglypuff", "Peach", "Daisy", "Bowser", "Ice Climbers", "Sheik", "Zelda", "Dr. Mario", "Pichu", "Falco", "Marth", "Lucina", "Young Link", "Ganondorf", "Mewtwo", "Roy", "Chrom", "Mr. Game & Watch", "Meta Knight", "Pit", "Dark Pit", "Zero Suit Samus", "Wario", "Snake", "Ike", "Pokemon Trainer", "Diddy Kong", "Lucas", "Sonic", "King Dedede", "Olimar", "Lucario", "R.O.B.", "Toon Link", "Wolf", "Villager", "Mega Man", "Wii Fit Trainer", "Rosalina & Luma", "Little Mac", "Greninja", "Mii Brawler", "Mii Swordfighter", "Mii Gunner", "Palutena", "Pac-Man", "Robin", "Shulk", "Bowser Jr.", "Duck Hunt", "Ryu", "Ken", "Cloud", "Corrin", "Bayonetta", "Inkling", "Ridley", "Simon", "Richter", "King K. Rool", "Isabelle", "Piranha Plant", "Joker", "Banjo & Kazooie")

def main_function():
    user_input = str(input("\n\nSelect a mode:\n\n|  Random (normal)\n|  Ditto\n|  Game\n\n|  "))

    if user_input.startswith("n"):
        if user_input == "n":
            print("\n" + all_fighters[random.randrange(0, 72)] + "\n" + all_fighters[random.randrange(0, 72)])
        elif user_input[1] in "123456789":
            count = int(user_input[1])
            print("\n")
            while count > 0:
                print(all_fighters[random.randrange(0, 72)])
                count -= 1
        elif user_input[2] in "123456789":
            count = int(user_input[2])
            print("\n")
            while count > 0:
                print(all_fighters[random.randrange(0, 72)])
                count -= 1
    ask()

def ask():
    input2 = str.lower(input("\n\nExit? (y/n)  "))
    if input2 == "y" or input2 == "yes":
        print("\nProgram was exited by user")
    elif input2 == "n" or input2 == "no":
        main_function()
    else:
        ask()

main_function()