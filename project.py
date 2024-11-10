from board import Board
import games

def choose_level():
    try:
        level_number = int(input("Enter level number (1-25): "))
        level_class_name = f"Level{level_number}"
        
        if hasattr(games, level_class_name):
            level_class = getattr(games, level_class_name)
            level = level_class()
            
        else:
            print("Invalid level number. Please enter a number between 1 an3d 24.")
    except ValueError:
        print("Please enter a valid number.")

choose_level()
