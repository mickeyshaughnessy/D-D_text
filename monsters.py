import random
from LLM import LLM

def generate_monster():
    monster_types = ['goblin', 'orc', 'skeleton', 'troll', 'dragon']
    monster_type = random.choice(monster_types)
    
    prompt = f"Create a brief description for a {monster_type} in a D&D adventure."
    description = LLM.complete(prompt, "ollama_llama2")
    
    return {
        'name': monster_type,
        'description': description,
        'health': random.randint(10, 100),
        'attack': random.randint(1, 20)
    }