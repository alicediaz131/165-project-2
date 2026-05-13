import requirements
import random

algos = [requirements.next_fit, requirements.first_fit, requirements.first_fit_decreasing, requirements.best_fit, requirements.best_fit_decreasing, ]

def generate_lists(n:int):
    items = []
    sum = 0
    for i in range(0,n):
        items.append(random.uniform(0.0, 0.65))
        sum += items[i]
    return items, [0]*len(items), [], sum


x = []
for i in range(11,31):
    x.append(int(2**(i/2)))
print(x)
for n in x:
    items, assignments, free_space, sum = generate_lists(n)
    for algo in algos:
        items_copy, assignments_copy, free_space_copy = items.copy(), assignments.copy(), free_space.copy()
        print(f'__________________________________________________')
        print(f'Testing: {algo.__name__} with input size {n}')
        algo(items_copy, assignments_copy, free_space_copy)
        print(f'Wasted % for {algo.__name__}: {round((1 - (sum/float(len(free_space_copy))))*100,3)}%')
        print(f'W({algo.__name__}): {round(float(len(free_space_copy))-sum,3)}')
