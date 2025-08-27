# scene_2.py

def play_scene():
    """
    Scene 2 Template:
    - Section A (Choice 1)
    - Section B (Choice 2)
    - Returns the name of the next scene (e.g., "scene_3") or "quit".
    """

    print("\n=== SCENE 2 ===")
    print("Section A: A cabin")
    
    choice_a = input("You can choose 'search' the area or 'move on': ").lower().strip()

    if choice_a == "search":
        print("You search carefully and find a lamp")
        # Placeholder logic
    elif choice_a == "move on":
        print("You decide to keep going with the lamp helping you see in the dark...")
        # Placeholder logic
    else:
        print("Unrecognized choice. You hesitate, but time moves on.")
    
    print("\n--- Moving to Section B of Scene 2 ---")
    print("Section B: Crystal Lake")
    
    choice_b = input("Do you 'investigate' the lake or 'ignore' and proceed forward? ").lower().strip()

    if choice_b == "investigate":
        print("You approach the lake cautiously...")
        return "scene_3"
    elif choice_b == "ignore":
        print("You choose to ignore the lake and continue...")
        return "scene_3"
    else:
        print("Unclear action. Let's assume you continue onward.")
        return "scene_3"

