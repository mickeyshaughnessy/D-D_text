import random
from character_sheet import create_character, display_character_sheet
from dungeons import generate_dungeon
from actions import get_available_actions, perform_action, quit_game
from monsters import generate_monster
from rules import check_rules
from LLM import LLM

def print_title():
    print(r"""
    ╔═══════════════════════════════════════════════╗
    ║ _____ ____ ____ ___ ______ __ ║
    ║ | __ | _ | _ \ | \ | __ | |/ _ ║
    ║ | | | | | | | | | | ) | | | | | \ \ ║
    ║ | | | | | | | | | | / / | | | | \ _ ║
    ║ | || | || | || | / / | || | / /(_)║
    ║ |_/|/|/ || |/ /_/ ║
    ║ ║
    ║ Text Adventure Game ║
    ╚═══════════════════════════════════════════════╝
    """)

def main():
    print_title()
    print("Welcome to the D&D Adventure! 🐉")
    character = create_character()
    display_character_sheet(character)
    print(f"You are {character['name']}, a level 1 {character['class']}. 🧙‍♂️")

    dungeon = generate_dungeon()
    print(f"You enter a {dungeon['type']} dungeon. 🏰")
    print(dungeon['description'])

    game_state = "You've just entered the dungeon."

    while True:
        print(f"\n{game_state}")
        actions = get_available_actions(character, dungeon, game_state)
        print("\nChoose an action:")
        for i, (shortcut, action) in enumerate(actions):
            print(f"{i+1}. {action.capitalize()}")

        while True:
            choice = input("> ")
            try:
                action_index = int(choice) - 1
                if 0 <= action_index < len(actions):
                    chosen_action = actions[action_index]
                    break
                else:
                    print("Invalid choice. Please enter a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if chosen_action == 'quit':
            print(quit_game())
            break

        result = perform_action(chosen_action, character, dungeon)
        print(f"\n{result}")

        game_state = result  # Update game state directly

        # Handle special events based on the action result
        if 'monster' in result.lower():
            monster = generate_monster()
            print(f"⚔️ You encounter a {monster['name']}!")
            print(monster['description'])
            fight_result = check_rules(character, monster)
            print(f"🏆 {fight_result}")
            game_state += f" {fight_result}"

        if 'treasure' in result.lower():
            treasure = random.choice(['gold', 'magic potion', 'enchanted weapon'])
            print(f"💎 You found some {treasure}!")
            game_state += f" You found {treasure}."

        if 'died' in result.lower():
            print("💀 Game Over!")
            break

if __name__ == "__main__":
    main()
