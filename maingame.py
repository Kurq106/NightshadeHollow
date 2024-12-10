import globalvars
from functions import collect_item, check_items, interact_with_familiar

def print_inventory():
    """
    Displays the player's inventory.
    """
    print("\n--- Current Inventory ---")
    if globalvars.items_list:
        print(", ".join(globalvars.items_list))
    else:
        print("Your inventory is empty.")

def start_game():
    """
    Greets the player and sets up the game.
    """
    print("Welcome to Nightshade Hollow!")
    globalvars.playername = input("Enter your character's name: ")
    print(f"Greetings, {globalvars.playername}! Your journey begins now.")
