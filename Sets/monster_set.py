import random
import time

'''🐉 “Monster Collector: The Quest for Rare Beasts”

Story:
You’re an adventurer exploring the mystical land of ByteVerse, capturing monsters.

Each monster is unique.

You can’t catch duplicates (the set takes care of that).

Random encounters happen each turn!'''

# List of possible monsters
all_monsters = [
    "Fire Drake", "Water Sprite", "Earth Golem", "Wind Wraith",
    "Thunder Tiger", "Shadow Panther", "Crystal Phoenix", "Lava Serpent"
]

# Your monster collection (set ensures uniqueness)
collection = set()

print("🐲 Welcome to Monster Collector: ByteVerse Edition!")
print("Catch monsters and complete your unique collection!\n")

while True:
    action = input("Press Enter to explore a new area (or type 'quit' to stop): ").lower()
    if action == "quit":
        print("\n🏆 Adventure Over!")
        break
    
    # Random encounter
    monster = random.choice(all_monsters)
    print(f"\n👀 You encountered a wild {monster}!")
    time.sleep(1)

    if monster in collection:
        print("❌ You already have this monster. It escaped!")
    else:
        collection.add(monster)
        print("✅ Monster caught! Added to your collection.")
    
    print(f"🎒 Your current collection ({len(collection)} monsters): {', '.join(collection)}\n")
    time.sleep(1)

print(f"\n🌟 Final Collection ({len(collection)} monsters): {', '.join(collection)}")
print("Thanks for playing Monster Collector! 🐉")
