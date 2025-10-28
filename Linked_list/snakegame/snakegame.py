import pygame
import random
import time
from collections import deque

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GREEN = (0, 200, 0)

class Node:
    """Node for the linked list representing snake body segments"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class LinkedList:
    """Linked List implementation for snake body"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append_left(self, x, y):
        """Add new segment to the head (for movement)"""
        new_node = Node(x, y)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def pop_right(self):
        """Remove tail segment"""
        if self.head is None:
            return None
        
        if self.head == self.tail:
            removed = self.head
            self.head = self.tail = None
            self.length = 0
            return removed
        
        current = self.head
        while current.next != self.tail:
            current = current.next
        
        removed = self.tail
        current.next = None
        self.tail = current
        self.length -= 1
        return removed
    
    def contains(self, x, y):
        """Check if position exists in the linked list (for collision detection)"""
        current = self.head
        while current:
            if current.x == x and current.y == y:
                return True
            current = current.next
        return False
    
    def get_positions(self):
        """Get all positions as list for rendering"""
        positions = []
        current = self.head
        while current:
            positions.append((current.x, current.y))
            current = current.next
        return positions

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Linked List Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.reset_game()
    
    def reset_game(self):
        """Initialize or reset game state"""
        self.snake = LinkedList()
        # Start with 3 segments in the middle
        start_x, start_y = GRID_WIDTH // 2, GRID_HEIGHT // 2
        for i in range(3):
            self.snake.append_left(start_x, start_y - i)
        
        self.direction = (0, -1)  # Start moving up
        self.next_direction = (0, -1)
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        self.speed = FPS
    
    def generate_food(self):
        """Generate food at random position not occupied by snake"""
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if not self.snake.contains(x, y):
                return (x, y)
    
    def handle_input(self):
        """Handle keyboard input for direction changes"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != (0, 1):
                    self.next_direction = (0, -1)
                elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                    self.next_direction = (0, 1)
                elif event.key == pygame.K_LEFT and self.direction != (1, 0):
                    self.next_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                    self.next_direction = (1, 0)
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()
        
        return True
    
    def update(self):
        """Update game state"""
        if self.game_over:
            return
        
        self.direction = self.next_direction
        
        # Calculate new head position
        head = self.snake.head
        new_x = (head.x + self.direction[0]) % GRID_WIDTH
        new_y = (head.y + self.direction[1]) % GRID_HEIGHT
        
        # Check collision with self using linked list traversal
        if self.snake.contains(new_x, new_y):
            self.game_over = True
            return
        
        # Add new head
        self.snake.append_left(new_x, new_y)
        
        # Check if food eaten
        if new_x == self.food[0] and new_y == self.food[1]:
            self.score += 10
            self.food = self.generate_food()
            # Increase speed slightly every 50 points
            if self.score % 50 == 0:
                self.speed += 1
        else:
            # Remove tail if no food eaten
            self.snake.pop_right()
    
    def draw(self):
        """Render game state"""
        self.screen.fill(BLACK)
        
        # Draw snake using linked list traversal
        positions = self.snake.get_positions()
        for i, (x, y) in enumerate(positions):
            color = GREEN if i == 0 else DARK_GREEN  # Head is brighter
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(self.screen, BLACK, rect, 1)  # Border
        
        # Draw food
        food_rect = pygame.Rect(self.food[0] * GRID_SIZE, self.food[1] * GRID_SIZE, 
                               GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(self.screen, RED, food_rect)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw linked list info
        list_info = self.font.render(f"Segments: {self.snake.length}", True, WHITE)
        self.screen.blit(list_info, (10, 50))
        
        # Draw game over message
        if self.game_over:
            game_over_text = self.font.render("GAME OVER! Press R to restart", True, WHITE)
            text_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            self.screen.blit(game_over_text, text_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(self.speed)
        
        pygame.quit()

# Run the games
if __name__ == "__main__":
    print("Choose a game to play:")
    print("1. Decision Tree Adventure Game")
    print("2. Linked List Snake Game")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        game = DecisionTreeGame()
        game.play()
    elif choice == "2":
        game = SnakeGame()
        game.run()
    else:
        print("Invalid choice!")