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

network = setup_village_network(roads)

for v1, v2 in network.items():
    print(f"Village {v1} is connected to: {' , '.join(v2)}")