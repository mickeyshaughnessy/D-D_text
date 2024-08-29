from LLM import LLM

def get_available_actions(character, dungeon, game_state):
    prompt = f"""
    In a D&D game:
    - The player is {character['name']}, a {character['class']}.
    - They are in a {dungeon['type']} dungeon.
    - Current game state: {game_state}

    Based on this context, what are 3-5 appropriate actions the player could take?
    Provide the actions as a comma-separated list of single words or short phrases.
    Include an appropriate emoji for each action.
    Always include 'quit' as an option with a 🚪 emoji.
    """
    
    response = LLM.complete(prompt, "ollama_llama2")
    actions = [action.strip() for action in response.split(',')]
    
    # Ensure 'quit' is always an option
    if not any('quit' in action.lower() for action in actions):
        actions.append('🚪 quit')
    
    # Add single-letter shortcuts
    actions_with_shortcuts = []
    for i, action in enumerate(actions):
        shortcut = action.split()[1][0].lower() if len(action.split()) > 1 else action[0].lower()
        actions_with_shortcuts.append((shortcut, action))
    
    return actions_with_shortcuts

def perform_action(action, character, dungeon):
    prompt = f"The {character['class']} {character['name']} is attempting to {action} in a {dungeon['type']} dungeon. Describe what happens."
    return LLM.complete(prompt, "ollama_llama2")

def quit_game(character, dungeon):
    return "You decide to end your adventure and return home. 🏠"