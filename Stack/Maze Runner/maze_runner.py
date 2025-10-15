import random
from collections import deque

# Maze dimensions
WIDTH, HEIGHT = 10, 10

# Generate maze grid (0 = empty, 1 = wall)
def generate_maze():
    maze = [[0 if random.random() > 0.2 else 1 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    maze[0][0] = 0   # Start
    maze[HEIGHT-1][WIDTH-1] = 0  # End
    return maze

# Print maze with player position
def print_maze(maze, player_pos):
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            if (y, x) == player_pos:
                row += "P "
            elif maze[y][x] == 1:
                row += "# "
            elif (y, x) == (HEIGHT-1, WIDTH-1):
                row += "E "
            else:
                row += ". "
        print(row)
    print()

# BFS pathfinder (optional hint)
def bfs_path(maze, start, end):
    queue = deque([start])
    visited = {start: None}
    while queue:
        y, x = queue.popleft()
        if (y, x) == end:
            path = []
            while (y, x) is not None:
                path.append((y, x))
                y, x = visited[(y, x)] if visited[(y, x)] else (None, None)
            return path[::-1]
        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = y+dy, x+dx
            if 0 <= ny < HEIGHT and 0 <= nx < WIDTH and maze[ny][nx] == 0 and (ny,nx) not in visited:
                visited[(ny,nx)] = (y,x)
                queue.append((ny,nx))
    return []

# Game loop
def play_maze():
    maze = generate_maze()
    player = (0, 0)
    end = (HEIGHT-1, WIDTH-1)
    print("Maze Runner! Reach 'E' to win. Controls: W/A/S/D")
    print_maze(maze, player)

    while player != end:
        move = input("Move: ").lower()
        y, x = player
        if move == "w": ny, nx = y-1, x
        elif move == "s": ny, nx = y+1, x
        elif move == "a": ny, nx = y, x-1
        elif move == "d": ny, nx = y, x+1
        else: continue
        if 0 <= ny < HEIGHT and 0 <= nx < WIDTH and maze[ny][nx] == 0:
            player = (ny, nx)
        print_maze(maze, player)
        if player == end:
            print("You won!")

if __name__ == "__main__":
    play_maze()
