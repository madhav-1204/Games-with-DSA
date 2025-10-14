from stack import Stack

class TowerOfHanoi:
    def __init__(self, num_disks=3):
        self.moves = 0
        self.num_disks = num_disks
        # Initialize the three towers as stacks
        self.towers = {
            'A': Stack('A'),
            'B': Stack('B'),
            'C': Stack('C')
        }
        
        # Initialize the first tower with disks
        for disk in range(num_disks, 0, -1):
            self.towers['A'].push(disk)
    
    def is_valid_move(self, from_tower, to_tower):
        if self.towers[from_tower].is_empty():
            return False
            
        if self.towers[to_tower].is_empty():
            return True
            
        return self.towers[from_tower].peek() < self.towers[to_tower].peek()
    
    def make_move(self, from_tower, to_tower):
        if self.is_valid_move(from_tower, to_tower):
            disk = self.towers[from_tower].pop()
            self.towers[to_tower].push(disk)
            self.moves += 1
            return True
        return False
    
    def is_solved(self):
        # Check if all disks are moved to tower C
        return (self.towers['C'].size() == self.num_disks and
                self.towers['A'].is_empty() and
                self.towers['B'].is_empty())
    
    def get_tower_state(self, tower_name):
        return self.towers[tower_name].get_items()
    
    def display(self):
        states = {}
        for tower in ['A', 'B', 'C']:
            states[tower] = self.get_tower_state(tower)
        
        # Find the maximum height
        max_height = max(len(state) for state in states.values())
        
        # Print the towers
        for level in range(max_height - 1, -1, -1):
            for tower in ['A', 'B', 'C']:
                if level < len(states[tower]):
                    print(f"[{states[tower][level]}]", end=" ")
                else:
                    print("| |", end=" ")
            print()
        print("-" * 20)
        print("A   B   C")

def play_game():
    # Example usage
    game = TowerOfHanoi(3)
    print("Welcome to Tower of Hanoi!")
    print("Move all disks from Tower A to Tower C.")
    print("Rules:")
    print("1. Move only one disk at a time")
    print("2. A larger disk cannot be placed on top of a smaller disk")
    print("\nInitial state:")
    game.display()
    
    while not game.is_solved():
        try:
            from_tower = input("\nMove from tower (A/B/C): ").upper()
            to_tower = input("Move to tower (A/B/C): ").upper()
            
            if from_tower not in ['A', 'B', 'C'] or to_tower not in ['A', 'B', 'C']:
                print("Invalid tower names! Use A, B, or C.")
                continue
                
            if game.make_move(from_tower, to_tower):
                print("\nCurrent state:")
                game.display()
                print(f"Moves made: {game.moves}")
            else:
                print("Invalid move! Try again.")
        except KeyboardInterrupt:
            print("\nGame terminated by user.")
            return
            
    print(f"\nCongratulations! You solved the puzzle in {game.moves} moves!")

if __name__ == "__main__":
    play_game()
