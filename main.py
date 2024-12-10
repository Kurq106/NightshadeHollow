import maingame
import globalvars
from functions import check_items

def main():
    # Initialize and start the game
    maingame.start_game()

    # Chapter imports
    import chapter1
    import chapter2
    import chapter3
    import chapter4
    import chapter5

    # Run chapters
    chapter1.main()
    chapter2.main()
    chapter3.main()
    chapter4.main()
    chapter5.main()

    # Check final success
    print("\n--- Grand Ritual ---")
    required_items = ["Earth Crystal", "Water Crystal", "Wind Crystal", "Fire Crystal"]
    if check_items(required_items, globalvars.items_list):
        print("The Grand Ritual is a success! You saved Nightshade Hollow.")
    else:
        print("You failed to gather all the items. Nightshade Hollow remains in peril.")

if __name__ == '__main__':
    main()
