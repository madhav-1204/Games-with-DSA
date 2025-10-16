import random

# Stack to store last few rounds
round_history = []

# Dictionary to define which move beats which
win_map = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def check_winner(player, computer):
    if player == computer:
        return "draw"
    elif win_map[player] == computer:
        return "player"
    else:
        return "computer"

def rps_game():
    moves = list(win_map.keys())
    score = {"player": 0, "computer": 0}
    max_history = 5  # Store only last 5 rounds

    print("🎮 Welcome to Rock, Paper, Scissors — DSA Edition!")
    print("Using a Stack to track your last few rounds...\n")

    while score["player"] < 3 and score["computer"] < 3:
        player = input("Enter your move (rock/paper/scissors): ").lower()
        if player not in moves:
            print("❌ Invalid move. Try again.\n")
            continue

        computer = random.choice(moves)
        print(f"🤖 Computer chose {computer}")

        result = check_winner(player, computer)
        if result == "draw":
            print("😐 It's a draw!\n")
        elif result == "player":
            print("🏆 You win this round!\n")
            score["player"] += 1
        else:
            print("💀 Computer wins this round!\n")
            score["computer"] += 1

        # Push result to the stack
        round_history.append((player, computer, result))
        if len(round_history) > max_history:
            round_history.pop(0)  # Maintain stack size

        print(f"Score: You {score['player']} - {score['computer']} Computer\n")

    if score["player"] == 3:
        print("🏆 You won the match!")
    else:
        print("🤖 Computer won the match!")

    print("\n Recent Game History :")
    for round_data in reversed(round_history):
        p, c, r = round_data
        print(f"  You: {p}, Computer: {c} -> {r.upper()}")

if __name__ == "__main__":
    rps_game()
