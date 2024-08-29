import random
from LLM import LLM

def create_character():
    classes = ['Warrior', 'Mage', 'Rogue', 'Cleric']
    races = ['Human', 'Elf', 'Dwarf', 'Halfling']
    
    character = {
        'name': input("Enter your character's name: "),
        'class': random.choice(classes),
        'race': random.choice(races),
        'strength': random.randint(8, 18),
        'dexterity': random.randint(8, 18),
        'constitution': random.randint(8, 18),
        'intelligence': random.randint(8, 18),
        'wisdom': random.randint(8, 18),
        'charisma': random.randint(8, 18)
    }
    
    prompt = f"Create a very brief backstory for a {character['race']} {character['class']} named {character['name']}."
    backstory = LLM.complete(prompt, "ollama_llama2")
    
    character['backstory'] = backstory
    
    return character

def display_character_sheet(character):
    print(f"\nCharacter Sheet for {character['name']}:")
    print(f"Race: {character['race']}")
    print(f"Class: {character['class']}")
    print(f"Strength: {character['strength']}")
    print(f"Dexterity: {character['dexterity']}")
    print(f"Constitution: {character['constitution']}")
    print(f"Intelligence: {character['intelligence']}")
    print(f"Wisdom: {character['wisdom']}")
    print(f"Charisma: {character['charisma']}")
    print(f"\nBackstory: {character['backstory']}")
