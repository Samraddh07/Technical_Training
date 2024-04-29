graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
]


from itertools import permutations


def find_routes(graph):
    min_path = float('inf')
    start = 0

    perms = permutations(range(start + 1, len(graph)))

    for path in perms:
        cost = 0

        j = start
        for i in path:
            cost += graph[j][i]
            j = i
        
        cost += graph[j][start]

        min_path = min(cost, min_path)

    
    return min_path

print(find_routes(graph))
        