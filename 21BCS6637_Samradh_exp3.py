stacks = []
for i in range(3):
    stacks.append(list(map(int, input(f'Enter the heights for stack {i}: ').split(' '))))

reverse_stacks = [l[::-1] for l in stacks]
partial_sum = []
for stack in reverse_stacks:
    sum_stack = [sum(stack[0:i+1]) for i in range(len(stack))]
    partial_sum.append(sum_stack)

common_elements = set(partial_sum[0]).intersection(*partial_sum[1:])
max_common_element = max(common_elements)
print('Maximum possible height:', max_common_element)