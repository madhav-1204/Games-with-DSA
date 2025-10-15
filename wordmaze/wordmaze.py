import random

# ---------- TRIE DATA STRUCTURE ----------
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end_of_word


# ---------- GAME ENGINE ----------
class WordMazeGame:
    def __init__(self, word_file="words.txt"):
        self.trie = Trie()
        with open(word_file, "r") as f:
            self.words = [w.strip().lower() for w in f.readlines()]
        for w in self.words:
            self.trie.insert(w)
        self.target_word = random.choice(self.words)
        self.attempts = 6
    
    def check_word(self, guess):
        feedback = []
        for i, ch in enumerate(guess):
            if i < len(self.target_word) and ch == self.target_word[i]:
                feedback.append("🟩")  # correct letter & position
            elif ch in self.target_word:
                feedback.append("🟨")  # correct letter wrong place
            else:
                feedback.append("⬜")  # wrong letter
        return "".join(feedback)

    def play(self):
        print("🎯 Welcome to WordMaze!")
        print("Guess the hidden word. You have 6 attempts.\n")

        for attempt in range(self.attempts):
            guess = input(f"Attempt {attempt+1}/{self.attempts}: ").lower()

            if not self.trie.search(guess):
                print("❌ Word not found in dictionary. Try again.\n")
                continue

            feedback = self.check_word(guess)
            print(f"Result: {feedback}\n")

            if guess == self.target_word:
                print(f"🏆 Congratulations! You guessed the word '{self.target_word}'!")
                return
        
        print(f"💀 Game Over! The correct word was '{self.target_word}'. Try again!\n")


# ---------- MAIN ----------
if __name__ == "__main__":
    game = WordMazeGame()
    game.play()
