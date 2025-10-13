

try:
    from game_logic import SnakeGame
    print("Successfully imported SnakeGame!")
except ImportError as e:
    print(f"Failed to import SnakeGame: {e}")
    # Optional: print content of game_logic.py to debug
    with open('game_logic.py', 'r') as f:
        print("\n--- Content of game_logic.py ---")
        print(f.read())
    print("----------------------------------")
except Exception as e:
    print(f"An unexpected error occurred: {e}")