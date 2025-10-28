import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player
player_size = 50
player_x = (SCREEN_WIDTH - player_size) / 2
player_y = SCREEN_HEIGHT - player_size - 10
player_speed = 5

# Enemy
enemy_size = 30
enemy_speed = 3
enemy_list = []

# Bullet
bullet_size = 10
bullet_speed = 7
bullet_list = []

# Score
score = 0
font = pygame.font.Font(None, 36)

# Functions to draw elements
def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, player_size, player_size))

def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, (x, y, enemy_size, enemy_size))

def draw_bullet(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, bullet_size, bullet_size))

def create_enemy():
    enemy_x = random.randint(0, SCREEN_WIDTH - enemy_size)
    enemy_y = 0
    enemy_list.append([enemy_x, enemy_y])

def create_bullet():
    bullet_x = player_x + player_size / 2 - bullet_size / 2
    bullet_y = player_y
    bullet_list.append([bullet_x, bullet_y])

def detect_collision(obj1_x, obj1_y, obj2_x, obj2_y, obj1_size, obj2_size):
    # This is a simplified collision check for rectangles
    if (obj1_x < obj2_x + obj2_size and
        obj1_x + obj1_size > obj2_x and
        obj1_y < obj2_y + obj2_size and
        obj1_y + obj1_size > obj2_y):
        return True
    return False

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                create_bullet()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
        player_x += player_speed

    # Enemy logic
    if random.randint(1, 100) < 5:  # Controls enemy spawn rate
        create_enemy()

    for enemy in enemy_list:
        enemy[1] += enemy_speed
        # Check for collision with player
        if detect_collision(player_x, player_y, enemy[0], enemy[1], player_size, enemy_size):
            running = False  # Game over

    # Bullet logic
    for bullet in bullet_list:
        bullet[1] -= bullet_speed
        # Check for collision with enemies
        for enemy in enemy_list:
            if detect_collision(bullet[0], bullet[1], enemy[0], enemy[1], bullet_size, enemy_size):
                enemy_list.remove(enemy)
                bullet_list.remove(bullet)
                score += 1
                break  # Exit inner loop after collision

    # Remove off-screen bullets and enemies
    bullet_list = [b for b in bullet_list if b[1] > 0]
    enemy_list = [e for e in enemy_list if e[1] < SCREEN_HEIGHT]

    # Drawing
    screen.fill(BLACK)
    draw_player(player_x, player_y)
    for enemy in enemy_list:
        draw_enemy(enemy[0], enemy[1])
    for bullet in bullet_list:
        draw_bullet(bullet[0], bullet[1])
    
    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
