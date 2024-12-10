def collect_item(item, items_list):
    """
    Adds an item to the player's inventory if it's not already there.
    """
    if item not in items_list:
        items_list.append(item)
        print(f"You have collected: {item}")
    else:
        print(f"You already have the {item} in your inventory.")

def check_items(required_items, items_list):
    """
    Checks if the player has all required items.
    """
    missing_items = [item for item in required_items if item not in items_list]
    if not missing_items:
        print("You have all the required items!")
        return True
    else:
        print(f"You are missing: {', '.join(missing_items)}")
        return False

def interact_with_familiar(familiar_name, items_list, item_reward):
    """
    Handles interaction with a familiar and rewards an item.
    """
    print(f"The {familiar_name} Familiar greets you.")
    response = input(f"Do you accept the {familiar_name} Familiar's help? (yes/no): ").lower()
    if response == "yes":
        collect_item(item_reward, items_list)
        return True
    else:
        print(f"You chose not to accept the {familiar_name} Familiar's help.")
        return False
