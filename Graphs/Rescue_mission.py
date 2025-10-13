from collections import deque


def rescue_mission(map, start_vlg, target_vlg):
    queue = deque([(start_vlg, [start_vlg])])

    visited = {start_vlg}

    while queue:
        cur, path = queue.popleft()

        if cur == target_vlg:
            return path
        
        for i in map.get(cur, []):
            if i not in visited:
                visited.add(i)
            
            new_path = path + [i]
            queue.append((i,new_path))

    return 'Path Not Found !!!!'


start = 'A'
target = 'D'

def setup_village_network(roads):
    nw = {}
    for i,j in roads:
        if i not in nw:
            nw[i]=[]
        nw[i].append(j)

        if j not in nw:
            nw[j] = []
        nw[j].append(i)
    return nw

roads=[
    ['A','B'],
    ['B','C'],
    ['D','C'],
    ['A','D']
]

map = setup_village_network(roads)

rescue_path = rescue_mission(map, start, target)

print(f"\n--- Rescue Mission from {start} to {target} ---")
if isinstance(rescue_path, list):
    print(f"Shortest path found in {len(rescue_path) - 1} steps:")
    print(" -> ".join(rescue_path))
else:
    print(rescue_path)