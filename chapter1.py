import globalvars

def main():
    print("\nWelcome to Nightshade Hollow!")
    print("Chapter 1: The Mystical Village")
    print("You arrive at Nightshade Hollow, a village brimming with magic.")
    globalvars.playername = input("What is your name, traveler? ")

    print(f"\nWelcome, {globalvars.playername}.")
    print("As you explore the village, you come across four glowing crystals.")
    print("Each crystal is linked to an elemental familiar:")
    print("1. Air (Guidance and agility)")
    print("2. Fire (Illumination and strength)")
    print("3. Earth (Treasure finding and endurance)")
    print("4. Water (Emotion and hidden pathways)")

    choice = input("Choose your familiar by typing its element: ").strip().lower()
    if choice in ["air", "fire", "earth", "water"]:
        globalvars.familiar = choice.capitalize()
        print(f"\nYou have bonded with the {globalvars.familiar} familiar!")
        globalvars.chapter1_success = True
    else:
        print("\nYou hesitate and fail to bond with any familiar. The village grows darker...")
        globalvars.chapter1_success = False

if __name__ == '__main__':
    main()
