import re
from collections import defaultdict

def word_frequency_game():
    print(" Welcome to the Word Frequency Detective Game! ")
    print("Enter any sentence — I'll secretly analyze it... \n")
    sentence = input("Type your sentence:\n> ").lower()
    words = re.findall(r'\b\w+\b', sentence)
    freq_map = defaultdict(int)
    for word in words:
        freq_map[word] += 1
    max_freq = max(freq_map.values())
    most_frequent_words = [word for word, freq in freq_map.items() if freq == max_freq]
    secret_word = most_frequent_words[0]  

    print("\n I’ve analyzed your sentence. Now guess...")
    print("Which word do you think appeared the most? ")
    guess = input("Your guess: ").lower()

    if guess == secret_word:
        print(f" Correct! The word '{secret_word}' appeared {max_freq} times!")
    elif guess in freq_map:
        print(f" Not quite. The most frequent word was '{secret_word}' ({max_freq} times).")
        print(f"Your guessed word '{guess}' appeared {freq_map[guess]} times.")
    else:
        print(f"'{guess}' didn’t even appear! The correct word was '{secret_word}'.")
    
    print("\n Word Frequency Table (Hash Map):")
    for word, freq in freq_map.items():
        print(f"{word:10} → {freq}")
        
word_frequency_game()
