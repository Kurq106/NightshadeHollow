import globalvars
import maingame

def main():
    if not globalvars.chapter1_success:
        print("\nYou cannot proceed without bonding with a familiar.")
        return

    print("\nChapter 2: Exploring Nightshade Hollow")
    print(f"With your {globalvars.familiar} familiar by your side, you begin exploring the village.")
    maingame.print_inventory(globalvars.inventory)

    # Add a challenge based on the chosen familiar
    if globalvars.familiar == "Air":
        print("You notice a hidden path leading into the woods. Your familiar guides you safely.")
        globalvars.inventory.append("Feather of Guidance")
    elif globalvars.familiar == "Fire":
        print("A cave looms ahead, its entrance dark and foreboding. Your familiar lights the way.")
        globalvars.inventory.append("Emberstone")
    elif globalvars.familiar == "Earth":
        print("Your familiar helps you uncover a hidden treasure beneath the soil.")
        globalvars.inventory.append("Golden Root")
    elif globalvars.familiar == "Water":
        print("Your familiar senses an underwater passage leading to a secret grotto.")
        globalvars.inventory.append("Pearl of Reflection")

    print("\nYou have obtained a special item!")
    maingame.print_inventory(globalvars.inventory)
    globalvars.chapter2_success = True

if __name__ == '__main__':
    main()
