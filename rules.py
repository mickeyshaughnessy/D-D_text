import random
from LLM import LLM

def roll_dice(sides=20):
    return random.randint(1, sides)

def check_rules(character, monster):
    player_roll = roll_dice()
    monster_roll = roll_dice()
    
    player_total = player_roll + (character['strength'] - 10) // 2
    monster_total = monster_roll + monster['attack']
    
    prompt = f"""
    In a D&D combat:
    - {character['name']} (a {character['class']}) rolled a {player_roll} with a strength modifier of {(character['strength'] - 10) // 2}, totaling {player_total}.
    - The {monster['name']} rolled a {monster_roll} with an attack bonus of {monster['attack']}, totaling {monster_total}.
    Describe the outcome of this combat round.
    """
    
    return LLM.complete(prompt, "ollama_llama2")