def binary_search_game():
    """
    A fun number guessing game that demonstrates the binary search algorithm.
    The computer will try to guess the number player has in mind between 1 and 100.
    It demonstrates how binary search efficiently finds the number in maximum 7 guesses.
    """
    print("\nWelcome to the Binary Search Number Guessing Game!")
    print("Think of a number between 1 and 100.")
    print("After each guess, tell me if the number is:")
    print("'h' - if your number is Higher")
    print("'l' - if your number is Lower")
    print("'c' - if my guess is Correct\n")

    left = 1
    right = 100
    attempts = 0
    
    while left <= right:
        attempts += 1
        mid = (left + right) // 2
        print(f"\nMy guess is: {mid}")
        response = input("Is your number higher (h), lower (l), or correct (c)? ").lower()
        
        if response == 'c':
            print(f"\nGreat! I found your number in {attempts} attempts!")
            print("This demonstrates the efficiency of binary search algorithm.")
            return
        elif response == 'h':
            left = mid + 1
        elif response == 'l':
            right = mid - 1
        else:
            print("Please enter 'h', 'l', or 'c'")
            attempts -= 1
            
    print("Something went wrong. Are you sure you didn't change your number? 🤔")

if __name__ == "__main__":
    while True:
        binary_search_game()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Hope you learned about binary search!")
            break