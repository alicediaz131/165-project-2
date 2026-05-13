import sys

def tim_sort (nums: list[int]):
    n = len(nums)

    
    runs = []
    ascending = True
    if nums[0] > nums[1]:
        ascending = False
    slicePoint = 0
    for i in range (1, n+1):
        if i == n:
            #print(nums[i-1])
            runs += [nums[slicePoint:i]]
        elif (nums[i-1] > nums[i]):
            if slicePoint+1 == i:
                ascending = False
            elif ascending == True:
                ascending = False
                runs += [nums[slicePoint:i]]
                slicePoint = i
        else:
            if slicePoint+1 == i:
                ascending = True
            elif ascending == False:
                ascending = True
                runs += [nums[slicePoint:i]]
                slicePoint = i
    stack = []
    #print(runs)
    #print(len(runs))
    #runLen = len(runs)
    comparisons = 0
    while len(runs) != 0:
        stack.insert(0, runs.pop(len(runs)-1))
        
        #print(len(stack))
        #print(runs)
        #print(f"printing stack of length: {len(stack)}: {stack}")
        while True:
            h = len(stack)
            if h >= 3 and len(stack[0]) > len(stack[2]):
                comparisons += merge(stack[1], stack[2])
                del stack[2]
            elif h >= 2 and len(stack[0]) >= len(stack[1]):
                comparisons += merge(stack[0], stack[1])
                #stack.pop(1)
                del stack[1]
            elif h >= 3 and len(stack[0]) + len(stack[1]) >= len(stack[2]):
                comparisons += merge(stack[0], stack[1])
                #stack.pop(1)
                del stack[1]
            elif h >= 4 and len(stack[1]) + len(stack[2]) >= len(stack[3]):
                comparisons += merge(stack[0], stack[1])
                del stack[1]
                #stack.pop(1)
            else:
                break
    while len(stack) != 1:
        comparisons += merge(stack[0], stack[1])
        #stack.pop(1)
        del stack[1]
    #print(stack[0])
    nums[:] = stack[0]
    return comparisons

def merge(l1: list[int], l2: list[int]):
    comparisons = 0

    l3 = []

    i1 = 0
    i2 = 0
    if l1[-1] > l1[0]:
        i1 = len(l1)-1
    if l2[-1] > l2[0]:
        i2 = len(l2)-1

    
    comparisons = comparer(l1, i1, l2, i2, l3)
    l1[:] = l3
    del l2
    #print(comparisons)
    #print(l1)
    return comparisons


def comparer(l1: list[int], i1: int, l2: list[int], i2: int, l3:list[int]):
    comparisons = 0
    while len(l1) != 0 or len(l2) != 0:
        if len(l1) != 0 and len(l2) != 0:
            comparisons += 1
            #print(f"comparing indexes i1: {i1} and i2: {i2} with values: {l1[i1]} and: {l2[i2]}")
        if len(l2) == 0 or (len(l1) != 0 and l1[i1] > l2[i2]):
            l3.append(l1.pop(i1))
            if i1 > 0:
                i1 -= 1
        else:
            l3.append(l2.pop(i2))
            if i2 > 0:
                i2 -= 1
            #print(f"comparisons: {comparisons}")
        #print(l3)
    return comparisons

    
# x4 = [ 42, 895, 231, 90, 8694, -21203, -24, 596, 723, -911, -100, 5382, 420, -502, 42, 895, 231, 90, 8694, -21203, -24, 596, 723, -911, -100, 5382, 420, -502, 42, 895, 231, 90, 8694, -21203, -24, 596, 723, -911, -100, 5382, 420]

# #x2 = [5, 2, 4, 1, 3, 11, 9, 8, 7, 6, 0, 10]
# tim_sort(x4)

# print(x4)
#print(f"comparisons: {tim_sort(x2)}")