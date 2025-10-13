# main.py

import tkinter as tk
from game_logic import SnakeGame

# --- Game Configuration ---
BOARD_WIDTH = 600
BOARD_HEIGHT = 400
SEGMENT_SIZE = 20 # Size of each snake segment and food square
GAME_SPEED = 150 # Milliseconds per frame update (lower = faster)

class SnakeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Linked List Snake Game")
        self.master.resizable(False, False)

        self.game = SnakeGame(BOARD_WIDTH, BOARD_HEIGHT, SEGMENT_SIZE)

        self.canvas = tk.Canvas(master, bg="black", 
                                width=BOARD_WIDTH, height=BOARD_HEIGHT)
        self.canvas.pack()

        self.score_label = tk.Label(master, text=f"Score: {self.game.score}", 
                                    font=('consolas', 16), bg="white", fg="black")
        self.score_label.pack(fill=tk.X)

        self.master.bind("<KeyPress>", self.on_key_press)
        
        self.draw_game()
        self.game_loop()

    def on_key_press(self, event):
        key = event.keysym
        if key in ['Up', 'Down', 'Left', 'Right']:
            self.game.change_direction(key)

    def draw_game(self):
        self.canvas.delete(tk.ALL) # Clear previous drawings

        # Draw food
        if self.game.food_pos:
            food_x, food_y = self.game.food_pos
            self.canvas.create_oval(food_x * SEGMENT_SIZE, food_y * SEGMENT_SIZE,
                                    (food_x + 1) * SEGMENT_SIZE, (food_y + 1) * SEGMENT_SIZE,
                                    fill="red", tags="food")

        # Draw snake (iterate through linked list segments)
        for i, (x, y) in enumerate(self.game.get_snake_segments()):
            color = "green" if i == 0 else "lime green" # Head is darker green
            self.canvas.create_rectangle(x * SEGMENT_SIZE, y * SEGMENT_SIZE,
                                         (x + 1) * SEGMENT_SIZE, (y + 1) * SEGMENT_SIZE,
                                         fill=color, tags="snake_segment")
        
        self.score_label.config(text=f"Score: {self.game.score}")

        if self.game.game_over:
            self.canvas.create_text(BOARD_WIDTH/2, BOARD_HEIGHT/2,
                                    font=('consolas', 40), text="GAME OVER", fill="white",
                                    tags="gameover")

    def game_loop(self):
        if not self.game.game_over:
            self.game.update()
            self.draw_game()
            self.master.after(GAME_SPEED, self.game_loop)
        else:
            # Optionally add a restart button or message
            pass

if __name__ == "__main__":
    root = tk.Tk()
    gui = SnakeGUI(root)
    root.mainloop()