#Function to find the spy in the village
def find_spy(villagers, friendships):
    friends = set(sum(friendships, []))
    return [v for v in villagers if v not in friends]


# llist of villagers in the village
villagers = ['A', 'B', 'C', 'D', 'E']
# List of friendships in the village in a pair 
friendships = [['A','B'], ['B','C'], ['C','D']]
print(find_spy(villagers, friendships))  
