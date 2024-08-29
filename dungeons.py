import random
from LLM import LLM

def generate_dungeon():
    dungeon_types = ['cave', 'ancient ruins', 'haunted castle', 'underground labyrinth']
    dungeon_type = random.choice(dungeon_types)
    
    prompt = f"Briefly escribe a {dungeon_type} dungeon for a D&D adventure."
    description = LLM.complete(prompt, "ollama_llama2")
    
    return {
        'type': dungeon_type,
        'description': description,
        'rooms': random.randint(5, 10)
    }

def describe_room():
    prompt = "Briefly describe a room in a dungeon for a D&D adventure."
    return LLM.complete(prompt, "ollama_llama2")
