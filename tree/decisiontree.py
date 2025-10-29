class DecisionNode:
    def __init__(self, description, options=None, outcomes=None):
        self.description = description
        self.options = options or []  # List of option texts
        self.outcomes = outcomes or []  # List of DecisionNode objects
        self.is_ending = False
        self.ending_message = ""
    
    def add_option(self, option_text, outcome_node):
        self.options.append(option_text)
        self.outcomes.append(outcome_node)
    
    def set_ending(self, message):
        self.is_ending = True
        self.ending_message = message

class DecisionTreeGame:
    def __init__(self):
        self.current_node = None
        self.game_over = False
        self.build_story_tree()
    
    def build_story_tree(self):
        # Create all story nodes
        start = DecisionNode("You wake up in a mysterious forest. The air is crisp and birds are chirping.")
        left_path = DecisionNode("You follow a narrow path to the left. It leads to an ancient castle.")
        right_path = DecisionNode("You take the right path and find a sparkling river.")
        
        castle_enter = DecisionNode("The castle gates are open. Do you enter?")
        castle_explore = DecisionNode("You walk around the castle walls and find a hidden garden.")
        river_cross = DecisionNode("The river looks shallow. Do you try to cross it?")
        river_follow = DecisionNode("You follow the river downstream.")
        
        # Endings
        treasure_ending = DecisionNode("")
        treasure_ending.set_ending("🎉 You found the royal treasure! You live happily ever after. YOU WIN!")
        
        dragon_ending = DecisionNode("")
        dragon_ending.set_ending("🔥 A dragon awakens and... well, let's just say it was quick. GAME OVER!")
        
        mermaid_ending = DecisionNode("")
        mermaid_ending.set_ending("🧜‍♀️ Friendly mermaids guide you to safety! You make it home safely. YOU WIN!")
        
        waterfall_ending = DecisionNode("")
        waterfall_ending.set_ending("💧 You slip on a wet rock and fall down a waterfall. GAME OVER!")
        
        # Build the tree structure
        start.add_option("Take the left path", left_path)
        start.add_option("Take the right path", right_path)
        
        left_path.add_option("Enter the castle", castle_enter)
        left_path.add_option("Explore around the castle", castle_explore)
        
        castle_enter.add_option("Search for treasure", treasure_ending)
        castle_enter.add_option("Investigate the throne room", dragon_ending)
        
        castle_explore.add_option("Rest in the garden", DecisionNode(""))
        castle_explore.outcomes[0].set_ending("🌿 You find peace in the beautiful garden and decide to stay forever. HAPPY ENDING!")
        
        right_path.add_option("Cross the river", river_cross)
        right_path.add_option("Follow the river downstream", river_follow)
        
        river_cross.add_option("Swim across", mermaid_ending)
        river_cross.add_option("Try to walk across the rocks", waterfall_ending)
        
        river_follow.add_option("Build a raft", DecisionNode(""))
        river_follow.outcomes[0].set_ending("🛶 Your raft takes you to a friendly village! YOU WIN!")
        
        self.current_node = start
    
    def display_current_situation(self):
        print("\n" + "="*50)
        print(self.current_node.description)
        
        if self.current_node.is_ending:
            print(f"\n{self.current_node.ending_message}")
            self.game_over = True
            return
        
        print("\nWhat do you do?")
        for i, option in enumerate(self.current_node.options, 1):
            print(f"{i}. {option}")
    
    def make_choice(self, choice):
        if self.game_over:
            print("The story has ended. Start a new game to play again!")
            return
        
        if 1 <= choice <= len(self.current_node.outcomes):
            self.current_node = self.current_node.outcomes[choice - 1]
        else:
            print("Invalid choice! Please select a valid option.")
    
    def play(self):
        print("🎮 WELCOME TO THE FOREST ADVENTURE! 🎮")
        print("Make choices by entering numbers. Your decisions shape the story!\n")
        
        while not self.game_over:
            self.display_current_situation()
            if self.game_over:
                break
            
            try:
                choice = int(input("\nEnter your choice (1-" + str(len(self.current_node.options)) + "): "))
                self.make_choice(choice)
            except ValueError:
                print("Please enter a valid number!")
        
        print("\n" + "="*50)
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again == 'y':
            self.__init__()  # Reset game
            self.play()

# Run the game
if __name__ == "__main__":
    game = DecisionTreeGame()
    game.play()