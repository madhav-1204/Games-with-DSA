"""
Tic-Tac-Toe (terminal) with Minimax AI.
Run: python3 tictactoe.py
"""

import math
import random
import sys
from typing import List, Optional, Tuple

# Board indices:
#  0 | 1 | 2
# -----------
#  3 | 4 | 5
# -----------
#  6 | 7 | 8

WIN_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)

def print_board(board: List[str]) -> None:
    def cell(i):
        return board[i] if board[i] != " " else str(i + 1)
    print()
    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")
    print()

def check_winner(board: List[str]) -> Optional[str]:
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None

def available_moves(board: List[str]) -> List[int]:
    return [i for i, v in enumerate(board) if v == " "]

def minimax(board: List[str], player: str, maximizing: bool, ai_player: str, human_player: str) -> Tuple[int, Optional[int]]:
    winner = check_winner(board)
    if winner == ai_player:
        return (1, None)
    elif winner == human_player:
        return (-1, None)
    elif winner == "Draw":
        return (0, None)

    if maximizing:
        best_score = -math.inf
        best_move = None
        for mv in available_moves(board):
            board[mv] = ai_player
            score, _ = minimax(board, player, False, ai_player, human_player)
            board[mv] = " "
            if score > best_score:
                best_score = score
                best_move = mv
        return (best_score, best_move)
    else:
        best_score = math.inf
        best_move = None
        for mv in available_moves(board):
            board[mv] = human_player
            score, _ = minimax(board, player, True, ai_player, human_player)
            board[mv] = " "
            if score < best_score:
                best_score = score
                best_move = mv
        return (best_score, best_move)

def ai_move(board: List[str], ai_player: str, human_player: str, difficulty: str) -> int:
    # difficulty: 'easy', 'medium', 'hard'
    moves = available_moves(board)
    if difficulty == "easy":
        return random.choice(moves)
    elif difficulty == "medium":
        # 50% optimal, 50% random
        if random.random() < 0.5:
            return random.choice(moves)
        _, move = minimax(board, ai_player, True, ai_player, human_player)
        return move if move is not None else random.choice(moves)
    else:  # hard: optimal
        _, move = minimax(board, ai_player, True, ai_player, human_player)
        return move if move is not None else random.choice(moves)

def ask_choice(prompt: str, choices: List[str]) -> str:
    choices_str = "/".join(choices)
    while True:
        ans = input(f"{prompt} ({choices_str}): ").strip().lower()
        if ans in choices:
            return ans
        print("Invalid choice. Try again.")

def ask_move(board: List[str]) -> int:
    moves = available_moves(board)
    while True:
        try:
            s = input("Your move (1-9): ").strip()
            if s.lower() in ("q", "quit", "exit"):
                print("Quitting.")
                sys.exit(0)
            mv = int(s) - 1
            if mv in moves:
                return mv
            else:
                print("That cell is not available. Choose another.")
        except ValueError:
            print("Please enter a number from 1 to 9 corresponding to an empty cell.")

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    mode = ask_choice("Choose mode: play vs AI or local two players", ["ai", "2p"])
    if mode == "ai":
        difficulty = ask_choice("Choose difficulty", ["easy", "medium", "hard"])
        marker = ask_choice("Do you want to be X or O", ["x", "o"])
        human_player = marker.upper()
        ai_player = "O" if human_player == "X" else "X"
        turn_order = ask_choice("Who goes first?", ["me", "ai"])
    else:
        difficulty = None
        human_player = "X"  # not used for 2p
        ai_player = "O"
        turn_order = "me"  # X starts

    board = [" "] * 9
    current = "X"  # X always starts in Tic-Tac-Toe

    print_board(board)

    while True:
        winner = check_winner(board)
        if winner:
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"Player {winner} wins!")
            break

        if mode == "2p":
            print(f"Player {current}'s turn.")
            mv = ask_move(board)
            board[mv] = current
        else:
            # vs AI
            if (current == human_player and turn_order == "me") or (current != human_player and turn_order == "ai" and current != ai_player):
                # This condition simplifies who is human based on choices; easier approach:
                pass

            if current == human_player:
                print("Your turn.")
                mv = ask_move(board)
                board[mv] = human_player
            else:
                print(f"AI ({difficulty}) is thinking...")
                mv = ai_move(board, ai_player, human_player, difficulty)
                board[mv] = ai_player
                print(f"AI plays at {mv + 1}.")

        print_board(board)
        current = "O" if current == "X" else "X"

    # play again?
    again = ask_choice("Play again?", ["y", "n"])
    if again == "y":
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nGoodbye!")
