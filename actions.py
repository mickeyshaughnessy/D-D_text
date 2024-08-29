from LLM import LLM

def get_available_actions(character, dungeon, game_state):
    prompt = f"""
    {character['name']}, a {character['class']}, is in a {dungeon['type']} dungeon.
    {game_state}

    Suggest 3-5 simple actions. 
    Format: action (emoji), action (emoji), ... 
    Include 'quit (🚪)' 
    """
    
    response = LLM.complete(prompt, "ollama_llama2")
    actions = [action.strip() for action in response.split(',')]
    
    # Ensure 'quit' is always an option
    if not any('quit' in action.lower() for action in actions):
        actions.append('quit (🚪)')
    
    # Add letters and format for display
    actions_with_letters = []
    letters = ['A', 'B', 'C', 'D', 'E']  # Adjust as needed
    for i, action in enumerate(actions):
        letter = letters[i]
        actions_with_letters.append(f"{letter}) {action}")

    return actions_with_letters


def perform_action(action, character, dungeon):
    prompt = f"{character['name']}, the {character['class']}, {action} in the {dungeon['type']} dungeon. What happens?"
    return LLM.complete(prompt, "ollama_llama2")

def quit_game(character, dungeon):
    return "You decide to end your adventure and return home. 🏠" 