import random
nodes, edges = list(map(int, input('Enter the nodes and edges: ').split(' ')))
graph = []
for i in range(edges):
    graph.append(list(map(int, input('Enter the Node From, Node To and Edge weight: ').split(' '))))

graph.sort(key=lambda x : x[2])
visited_nodes = {}
for paths in graph:
    u, v, weight = paths
    if v in sum(list(visited_nodes.values()), []):
        continue

    if weight in visited_nodes.keys():
        old_u, old_v = visited_nodes[weight]
        if (u + v + weight) < (old_u + old_v + weight):
            visited_nodes[weight] = [u, v]
        elif  (u + v + weight) == (old_u + old_v + weight):
            u, v = random.choice([[u, v],[old_u, old_v]])
            visited_nodes[weight] = [u, v]
        else:
            continue
    
    visited_nodes[weight] = [u, v]

print(sum(visited_nodes.keys()))

