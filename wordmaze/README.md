# 🎮 WordMaze – Data Structure Game (Trie + Algorithm)

A fun CLI-based word guessing game built using **Trie Data Structure** and **Algorithmic Word Matching Logic**.

## 🚀 How It Works
- The game loads a list of words from `words.txt`
- It stores them inside a Trie for fast lookup (O(length of word))
- The player guesses the hidden word within 6 tries
- The program gives feedback:
  - 🟩 correct letter, correct position  
  - 🟨 correct letter, wrong position  
  - ⬜ incorrect letter  

## 🧠 Concepts Used
- **Trie (Prefix Tree)** for word validation  
- **String Matching Algorithm** for feedback  
- **Random Selection & Input Handling**

## 💡 How to Run
```bash
python3 wordmaze.py
