import heapq
import random
import time

class DeliveryCenter:
    def __init__(self):
        self.tasks = []
        self.counter = 1  
    
    def add_delivery(self, priority, description):
        heapq.heappush(self.tasks, (priority, self.counter, description))
        print(f"📦 New delivery added (Priority {priority}): {description}")
        self.counter += 1

    def dispatch_delivery(self):
        if self.tasks:
            priority, _, description = heapq.heappop(self.tasks)
            print(f"\n🤖 Robot dispatched for: {description} (Priority {priority})")
            event = random.choice([
                "✅ Delivery successful! Customer is happy.",
                "⚡ Robot ran out of battery mid-route!",
                "🚧 Traffic jam delayed delivery.",
                "🎉 Bonus points! Customer tipped extra credits."
            ])
            print(f"🗞️ Status: {event}\n")
        else:
            print("😴 No deliveries left! All robots are recharging.\n")

def game():
    print("🚀 Welcome to *Robot Delivery Rush*!")
    print("Manage your robots wisely — urgent tasks first!\n")

    center = DeliveryCenter()

    deliveries = [
        ("Deliver medicine to Sector 9", 1),
        ("Send pizza to Tech Hub", 3),
        ("Deliver spare parts to Factory 22", 2),
        ("Ship memes to Galactic Forum", 5),
        ("Recharge station batteries", 4)
    ]

    
    for desc, prio in deliveries:
        center.add_delivery(prio, desc)
        time.sleep(0.5)

    print("\n--- Dispatching Begins ---\n")
    time.sleep(1)

    while center.tasks:
        center.dispatch_delivery()
        time.sleep(1)

    print("🏁 All deliveries completed! The city runs smoothly again.\n")

# Run the game
game()
