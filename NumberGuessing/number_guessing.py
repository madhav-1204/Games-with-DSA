import random

def number_guessing_game():
    """
    Number Guessing Game
    Player tries to guess a randomly generated number between 1 and 100.
    Tracks attempts and gives feedback if guess is too high or too low.
    """
    
    print("🎮 Welcome to the Number Guessing Game! 🎮")
    print("I have picked a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible!\n")
    
    # Random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    # Game loop
    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < 1 or user_guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
                continue
            
            if user_guess < number_to_guess:
                print("⬆️ Too low! Try a higher number.")
            elif user_guess > number_to_guess:
                print("⬇️ Too high! Try a lower number.")
            else:
                guessed = True
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")

    # Option to replay
    replay = input("\nDo you want to play again? (y/n): ").strip().lower()
    if replay == 'y':
        print("\nStarting a new game...\n")
        number_guessing_game()
    else:
        print("\nThanks for playing! Goodbye 👋")

# Run the game if this file is executed
if __name__ == "__main__":
    number_guessing_game()