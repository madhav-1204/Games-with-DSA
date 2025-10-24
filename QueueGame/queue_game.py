# 🎯 Queue Game
# Author: Rana Shivang Singh
# Description: A small interactive console-based game demonstrating the Queue (FIFO) concept in Python.
# Data Structure Used: deque (from collections)
# ---------------------------------------------------------
# Rules:
# - Players join the queue (Enqueue)
# - The first player to join gets to play first (Dequeue)
# - You can view the current queue anytime
# - Exit when you're done having fun!

from collections import deque

# Initialize an empty queue
player_queue = deque()

print("\n🎮 Welcome to the Queue Game!")
print("Players will join the queue and play in FIFO order (First In, First Out).")

# Game loop starts
while True:
    # Display menu options
    print("\n===== MENU =====")
    print("1️⃣  Join Game (Enqueue)")
    print("2️⃣  Play Turn (Dequeue)")
    print("3️⃣  Show Queue")
    print("4️⃣  Exit Game")
    print("=================")

    choice = input("👉 Enter your choice (1-4): ")

    # Option 1: Enqueue player
    if choice == "1":
        name = input("Enter player name: ")
        player_queue.append(name)
        print(f"✅ {name} has joined the queue!")

    # Option 2: Dequeue player
    elif choice == "2":
        if player_queue:
            current_player = player_queue.popleft()
            print(f"🎯 {current_player} is now playing the game!")
        else:
            print("⚠️  No players in queue! Add players first.")

    # Option 3: Show queue
    elif choice == "3":
        if player_queue:
            print("🧍 Current Queue:", " → ".join(player_queue))
        else:
            print("🚫 Queue is empty!")

    # Option 4: Exit
    elif choice == "4":
        print("👋 Thanks for playing the Queue Game!")
        break

    # Invalid choice
    else:
        print("❌ Invalid input! Please choose between 1–4.")

# End of Game

