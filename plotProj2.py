import requirements
import random
#import multiprocessing as mp
#from numba import jit, prange
from multiprocessing import Pool

import matplotlib.pyplot as plt

import random, math, time, csv
import numpy as np
from sklearn.metrics import r2_score
algos = [requirements.next_fit, requirements.first_fit, requirements.first_fit_decreasing, requirements.best_fit, requirements.best_fit_decreasing, ]

colors = ['red', 'blue', 'green', 'purple', 'orange']

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
        print("in algo")
        x, y = [], []
        outputname = algos[algo].__name__ + '.csv'
        with open(outputname, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                x.append(float(row[0]))
                y.append(float(row[1]))

        
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
    plt.show()
plotFunc([0,1,2,3,4])


def plotFunc2(functionIndex: int, cut=0):
    colorIndex = 0
    x, y = [], []
    outputname = algos[functionIndex].__name__ + '.csv'
    with open(outputname, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                x.append(float(row[0]))
                y.append(float(row[1]))
            
    #plt.loglog(x, y, linestyle = 'None', marker='o', base=2, color=colors[colorIndex])
    p = plt.loglog(x, y, linestyle = 'None', marker='o', base=2, color=colors[colorIndex])
    logx, logy = np.log(x), np.log(y)
    logx_fit = logx[cut:]
    logy_fit = logy[cut:]

    m, b = np.polyfit(logx_fit, logy_fit, 1)
    fit = np.poly1d((m, b))
    expected_logy = fit(logx)
    r2 = r2_score(logy, expected_logy)
    residuals = logy - expected_logy
    print(np.max(np.abs(residuals)))

    #plt.loglog(x[::len(x)-1], (math.e ** expected_logy)[::len(y)-1], '--', label=f'{myFunctions[functionIndex].__name__}: {round(m, 2):0.5} log n + {round(b, 2):.5}, r^2 = {round(r2,3):.5}', color=colors[colorIndex], base=2)
    plt.loglog(x[cut:], np.exp(expected_logy[cut:]), '--', f'{round(m, 2):0.5} log n + {round(b, 2):.5}, r^2 = {round(r2,4):.5}', color=colors[colorIndex], base=2)
    #plt.loglog(x[cut:], np.exp(expected_logy[cut:]), '--', label=f'{listtype}: {round(m, 2):0.5} log n + {round(b, 2):.5}, r^2 = {round(r2,4):.5}', color=colors[colorIndex], base=2)

    plt.xlabel("Log N (# of elements)", fontsize="large")
    plt.ylabel("Log W(N) ", fontsize="large")
    plt.title('Plotting Waste with ' + algos[functionIndex].__name__ + '()', fontsize = 15) 

    plt.legend()
    colorIndex += 1
    plt.show()

#for algo in range (len(algos)):
    #plotFunc2(algo)
   
