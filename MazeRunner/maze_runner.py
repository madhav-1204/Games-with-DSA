import sys
import collections

class Maze:
    def __init__(self, grid):
        """
        grid: list of list of str, where
            '#' means wall,
            '.' means open space,
            'S' means start,
            'G' means goal.
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = None
        self.goal = None
        self._find_special_cells()
        self.graph = self._build_graph()

    def _find_special_cells(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 'S':
                    self.start = (r, c)
                elif self.grid[r][c] == 'G':
                    self.goal = (r, c)
        if self.start is None or self.goal is None:
            raise ValueError("Grid must have one 'S' (start) and one 'G' (goal)")

    def _build_graph(self):
        # adjacency list: map (r,c) -> list of neighbor (r2,c2)
        graph = {}
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] != '#':
                    neighbours = []
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] != '#':
                            neighbours.append((nr, nc))
                    graph[(r, c)] = neighbours
        return graph

    def bfs_shortest_path(self):
        """Return the shortest path from start to goal as list of (r,c), or None if no path."""
        queue = collections.deque([self.start])
        visited = {self.start: None}  # map cell -> previous cell
        while queue:
            current = queue.popleft()
            if current == self.goal:
                # reconstruct path
                path = []
                node = current
                while node is not None:
                    path.append(node)
                    node = visited[node]
                path.reverse()
                return path
            for neighbour in self.graph.get(current, []):
                if neighbour not in visited:
                    visited[neighbour] = current
                    queue.append(neighbour)
        return None

    def print_grid_with_path(self, path):
        """Print the maze grid, marking the path with '*'."""
        grid_copy = [list(row) for row in self.grid]
        for (r, c) in path:
            if grid_copy[r][c] not in ('S', 'G'):
                grid_copy[r][c] = '*'
        for row in grid_copy:
            print(''.join(row))

    def play(self):
        print("Welcome to Maze Runner!")
        print("Controls: W = up, S = down, A = left, D = right. Q = quit.")
        print("Find the goal 'G' from the start 'S'. Walls are '#'.")
        player_pos = self.start
        while True:
            for r in range(self.rows):
                row = "".join(self.grid[r][c] if (r, c) != player_pos else 'P'
                              for c in range(self.cols))
                print(row)
            if player_pos == self.goal:
                print("Congratulations! You've reached the goal!")
                break
            move = input("Move (W/A/S/D/Q): ").strip().upper()
            if move == 'Q':
                print("Thanks for playing. Goodbye!")
                break
            delta = {'W':(-1,0), 'S':(1,0), 'A':(0,-1), 'D':(0,1)}.get(move)
            if delta is None:
                print("Invalid input. Use W/A/S/D/Q.")
                continue
            nr = player_pos[0] + delta[0]
            nc = player_pos[1] + delta[1]
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] != '#':
                player_pos = (nr, nc)
            else:
                print("Blocked by wall or outside maze. Choose another direction.")
        # After game end, show the optimal path:
        path = self.bfs_shortest_path()
        if path:
            print("\nOptimal shortest path from 'S' to 'G' (marked with '*'):")
            self.print_grid_with_path(path)
        else:
            print("No possible path from start to goal in this maze.")

def main():
    sample_grid = [
        "##########",
        "#S...#...#",
        "#.#.#.#..#",
        "#.#.#.##.#",
        "#...#....#",
        "#.####.#G#",
        "##########",
    ]
    grid = [list(row) for row in sample_grid]
    maze = Maze(grid)
    maze.play()

if __name__ == "__main__":
    main()
