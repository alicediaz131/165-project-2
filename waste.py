import requirements
import random
import os
#import multiprocessing as mp
#from numba import jit, prange
from multiprocessing import Pool
colors = ['red', 'blue', 'green', 'purple', 'orange']
import matplotlib.pyplot as plt

import random, math, time, csv
import numpy as np
from sklearn.metrics import r2_score
algos = [requirements.next_fit, requirements.first_fit, requirements.first_fit_decreasing, requirements.best_fit, requirements.best_fit_decreasing, ]




x = []
#for i in range(11,15):
j = 105
for i in range(12,40+1):
    if j > 10:
        j = j - 5
    x.append([int(2**(i/2)), i/2, j])
print(x)

#data_3d = [[[0 for _ in range(0)] for _ in range(3)] for _ in range(len(algos))]

def generate_lists(n:int):
    items = []
    sum = 0
    for i in range(0,n):
        items.append(random.uniform(0.0, 0.65))
        sum += items[i]
    return items, [0]*len(items), [], sum

def trial(args):
    alg, n = args
    #print(alg)
    #print(n)
    items, assignments, free_space, total_sum = generate_lists(n)
    items_copy, assignments_copy, free_space_copy = items.copy(), assignments.copy(), free_space.copy()
    #print(f'{algos[alg].__name__} with input size 2^{j} test {i+1} of {j}')
    algos[alg](items_copy, assignments_copy, free_space_copy)
    #avg_waste_percentage += (1 - (sum/float(len(free_space_copy))))*100
    #avg_waste += float(len(free_space_copy))- sum
    return float(len(free_space_copy))-total_sum, float((1 - (total_sum/float(len(free_space_copy))))*100)

def recordWaste(alg):
    #for alg in range(len(algos)):
    outputname = algos[alg].__name__ + '.csv'
    with open(outputname, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        rows = []
        for n in x:
            avg_waste_percentage = 0.0
            avg_waste = 0.0
            print(f'__________________________________________________')
            print(f'Testing: {algos[alg].__name__} with input size 2^{n[1]} for {n[2]} iterations')
            with Pool(8) as p:
                results = p.map(trial, [(alg, n[0]) for __ in range(n[2])])

            # for i in range(n[2]):
            #     items, assignments, free_space, sum = generate_lists(n[0])
            #     items_copy, assignments_copy, free_space_copy = items.copy(), assignments.copy(), free_space.copy()
            #     #print(f'__________________________________________________')
            #     print(f'{algos[alg].__name__} with input size 2^{n[1]} test {i+1} of {n[0]}')
            #     algos[alg](items_copy, assignments_copy, free_space_copy)
            #     #print(items, assignments, free_space)

            #     #print(f'bins used: {len(free_space_copy)}, sum: {sum}')
            #     #print(f'Wasted % for {algos[alg].__name__}: {round((1 - (sum/float(len(free_space_copy))))*100,3)}%')
            #     #print(f'W({algos[alg].__name__}): {round(float(len(free_space_copy))-sum,3)}')
            #     avg_waste_percentage += (1 - (sum/float(len(free_space_copy))))*100
            #     avg_waste += float(len(free_space_copy))- sum

            #avg_waste_percentage = avg_waste_percentage/n[2]
            #avg_waste = avg_waste/n[2]
            avg_waste = sum(r[0] for r in results) / n[2]
            avg_waste_percentage = sum(r[1] for r in results) / n[2]
            print(f'W({algos[alg].__name__}) avg: {avg_waste}')
            print(f'Wasted % for {algos[alg].__name__} avg: {avg_waste_percentage}%')
            rows.append([n[0], avg_waste, avg_waste_percentage])
        #writer.writeheader
        writer.writerows(rows)

#if __name__ == '__main__':
    #with Pool(len(algos)) as p:
        #p.map(recordWaste, [0,1,2,3,4])
if __name__ == '__main__':
    for alg in range(len(algos)):
        recordWaste(alg)



#for alg in range(len(algos)):
#with mp.Pool() as pool:
   # pool.map(recordWaste, range(len(algos)))



# for i in range(len(myFunctions)):
#     for j in range(3):
#         listtype = ""
#         match j:
#             case 0:
#                 listtype = "Uniformly Random"
#             case 1:
#                 listtype = "Almost Sorted"
#             case 2:
#                 listtype = "Two Alternating"
#         outputname = myFunctions[i].__name__ + ' ' + listtype + '.csv'
#         with open(outputname, 'w', newline='') as f:
#             writer = csv.writer(f)
#             writer.writerows(data_3d[i][j])


def plotFunc(algoIndices: list[int], cut=0):
    # match listIndex:
    #         case 0:
    #             listtype = "Uniformly Random"
    #         case 1:
    #             listtype = "Almost Sorted"
    #         case 2:
    #             listtype = "Two Alternating"

    colorIndex = 0
    for algo in algoIndices:
        x, y = [], []
        outputname = algos[algo].__name__ + '.csv'
        with open(outputname, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                x.append(float(row[1]))
                y.append(float(row[2]))

        
        #scatter plot
        p = plt.loglog(x, y, linestyle = 'None', marker='o', base=2, color=colors[colorIndex])
        




        logx, logy = np.log(x), np.log(y)

        logx_fit = logx[cut:]
        logy_fit = logy[cut:]
        

        m, b = np.polyfit(logx_fit, logy_fit, 1)
        fit = np.poly1d((m, b))
        expected_logy = fit(logx)
        r2 = r2_score(logy, expected_logy)


        #plt.loglog(x[::len(x)-1], (math.e ** expected_logy)[::len(y)-1], '--', label=f'{myFunctions[functionIndex].__name__}: {round(m, 2):0.5} log n + {round(b, 2):.5}, r^2 = {round(r2,3):.5}', color=colors[colorIndex], base=2)
        plt.loglog(x[cut:], np.exp(expected_logy[cut:]), '--', label=f'{algos[algo].__name__}: {round(m, 2):0.5} log n + {round(b, 2):.5}, r^2 = {round(r2,3):.5}', color=colors[colorIndex], base=2)
        
        plt.xlabel("Log N (# of elements)", fontsize="large")
        plt.ylabel("Log Waste(N) ", fontsize="large")
        #plt.title('Sorting ' + listtype + ' Permutations using Different Sorting Functions', fontsize = 15) 

        plt.legend()
        colorIndex += 1

#plotFunc([0,1,3])