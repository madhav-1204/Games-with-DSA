# game_logic.py

import random
from linked_list import DoublyLinkedList

class SnakeGame:
    def __init__(self, board_width, board_height, segment_size):
        self.board_width = board_width
        self.board_height = board_height
        self.segment_size = segment_size
        self.score = 0
        self.game_over = False

        self.snake_body = DoublyLinkedList()
        self.direction = 'Right' # Initial direction
        self.food_pos = None

        self._initialize_game()

    def _initialize_game(self):
        # Start snake in the middle
        start_x = self.board_width // (2 * self.segment_size)
        start_y = self.board_height // (2 * self.segment_size)
        self.snake_body.insert_at_head((start_x, start_y))
        
        self.place_food()

    def _get_head_coords(self):
        # The head is always the data in the first node of the linked list
        return self.snake_body.head.data

    def _get_new_head_position(self):
        head_x, head_y = self._get_head_coords()
        if self.direction == 'Up':
            new_head_x, new_head_y = head_x, head_y - 1
        elif self.direction == 'Down':
            new_head_x, new_head_y = head_x, head_y + 1
        elif self.direction == 'Left':
            new_head_x, new_head_y = head_x - 1, head_y
        elif self.direction == 'Right':
            new_head_x, new_head_y = head_x + 1, head_y
        return (new_head_x, new_head_y)

    def place_food(self):
        # Ensure food doesn't spawn on the snake
        while True:
            food_x = random.randint(0, (self.board_width // self.segment_size) - 1)
            food_y = random.randint(0, (self.board_height // self.segment_size) - 1)
            new_food_pos = (food_x, food_y)
            if new_food_pos not in self.snake_body.get_all_data():
                self.food_pos = new_food_pos
                break

    def change_direction(self, new_direction):
        if new_direction == 'Up' and self.direction != 'Down':
            self.direction = 'Up'
        elif new_direction == 'Down' and self.direction != 'Up':
            self.direction = 'Down'
        elif new_direction == 'Left' and self.direction != 'Right':
            self.direction = 'Left'
        elif new_direction == 'Right' and self.direction != 'Left':
            self.direction = 'Right'

    def update(self):
        if self.game_over:
            return

        new_head_pos = self._get_new_head_position()
        
        # Check for collisions
        if (new_head_pos[0] < 0 or new_head_pos[0] >= (self.board_width // self.segment_size) or
            new_head_pos[1] < 0 or new_head_pos[1] >= (self.board_height // self.segment_size)):
            self.game_over = True # Hit wall
            return
        
        # Check for self-collision (don't check the tail, as it's about to move)
        if new_head_pos in self.snake_body.get_all_data()[:-1]: # Check all body parts except the last (tail)
            self.game_over = True # Hit self
            return
            
        # Move snake: Add new head
        self.snake_body.insert_at_head(new_head_pos)

        # Check if food was eaten
        if new_head_pos == self.food_pos:
            self.score += 1
            self.place_food() # Place new food
        else:
            self.snake_body.remove_from_tail() # If no food, remove tail to maintain length
            
        # If the snake became empty somehow (shouldn't happen with proper logic)
        if self.snake_body.is_empty():
            self.game_over = True


    def get_snake_segments(self):
        return self.snake_body.get_all_data()