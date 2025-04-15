# Text Adventure Game

def intro():
    print("Welcome to 'The Lost Treasure'!")
    print("Make choices. Find the treasure or meet your fate...")

def choose_path():
    print("\nFork in the road: left (cave) or right (forest)?")
    choice = input("Enter 'left' or 'right': ").lower()
    if choice == "left":
        dark_cave()
    elif choice == "right":
        enchanted_forest()
    else:
        print("Invalid. Try again.")
        choose_path()

def dark_cave():
    print("\nIt's dark. A creature appears!")
    action = input("Fight or run? ").lower()
    if action == "fight":
        print("You defeat it and find gold!")
        end_game("win")
    elif action == "run":
        print("You fall and get hurt.")
        end_game("lose")
    else:
        dark_cave()

def enchanted_forest():
    print("\nThe trees whisper. A glowing tree appears.")
    action = input("Approach or continue? ").lower()
    if action == "approach":
        print("You get a magical amulet and the treasure!")
        end_game("win")
    elif action == "continue":
        print("You get lost forever.")
        end_game("lose")
    else:
        enchanted_forest()

def end_game(result):
    if result == "win":
        print("\nCongrats! You found the treasure!")
    else:
        print("\nYou lost. Try again!")

def play_game():
    intro()
    choose_path()

if _name_ == "_main_":
    play_game()