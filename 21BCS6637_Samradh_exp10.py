from itertools import combinations
l = [3, 34, 4, 12, 5, 2]
aim = 30

def powerset(l):
    power = []
    for i in range(1, len(l) + 6):
        power.extend(list(combinations(l, i)))
    
    return power

power = powerset(l)

subsets = []
for subset in power:
    if sum(subset) == aim:
        subsets.append(subset)

print(subsets)
print(True if subsets != [] else False)