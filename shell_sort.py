import math
import heapq


def shell_sort1(nums:list[int]):
    n = int(len(nums))
    gap = int(math.floor(n/2))
    comparisons = 0
    while (gap > 0): #log n times...
        comparisons += shell_sort_gapped(nums, gap, n)
        gap = int(gap/2) #k doesnt exist in this version, it's computed by consistently changing gaps value here
    return comparisons

def shell_sort2(nums:list[int]):
    n = int(len(nums))
    logn = int(math.floor(math.log2(n))) #used floor function here to match assignment specs. +1 will be needed in for loop later
    comparisons = 0
    for k in range(1, logn+1, 1): #could be an issue that k isn't a real number. I doubt it will be, but we'll see...
        gap = 2*int(math.floor(n/2**(k+1)))+1
        comparisons += shell_sort_gapped(nums, gap, n)
    return comparisons

def shell_sort3(nums:list[int]):
    n = int(len(nums))
    logn = int(math.log2(n)) #used floor function here to match assignment specs. +1 will be needed in for loop later
    comparisons = 0
    for k in range(logn, -1, -1):
        gap = int(2**k)+1
        #print(gap)
        if k == 0:
            gap = 1
        comparisons += shell_sort_gapped(nums, gap, n)
    return comparisons


def shell_sort4(nums:list[int]):
    n = int(len(nums))
    smoothNums = [1]
    i = 0
    i2 = 0
    i3 = 0
    next2 = 2
    next3 = 3
    while (next2 < n or next3 < n):
        next = min(next2,next3)
        smoothNums.append(next)
        if next == next2:
            i2 += 1
            next2 = smoothNums[i2] * 2
        if next == next3:
            i3 += 1
            next3 = smoothNums[i3] * 3
        i += 1
    comparisons = 0
    for gap in reversed(smoothNums):
            comparisons += shell_sort_gapped(nums, gap, n)
    return comparisons

def shell_sort5(nums: list[int]):
    n = int(len(nums))

    #(3^n - 1)/2. 
    sequence = []
    index = 1
    while (index < n):
        x = (int)((3**index - 1)/2)
        if x < n:
            sequence.append(x)
            index += 1
        else:
            break
    #print(sequence)
    comparisons = 0
    for k in range(len(sequence)-1, -1, -1):
        gap = sequence.pop()
        comparisons += shell_sort_gapped(nums, gap, n)
    return comparisons

def shell_sort6(nums: list[int]):
    n = int(len(nums))

    #(3^n - 1)/2. 
    sequence = []
    index = 1
    while (index < n):
        x = (int)((3**index - 1)/2)
        if x < n:
            sequence.append(x)
            index += 1
        else:
            break
    #print(sequence)
    comparisons = 0
    for k in range(len(sequence)-1, -1, -1):
        gap = sequence.pop()
        comparisons += shell_sort_gapped_descending(nums, gap, n)
    return comparisons

def shell_sort_gapped(nums: list[int], gap, n):
    comparisons = 0
    for i in range (gap, n, 1): 
            temp = nums[i] 
            j = i 
            while j >= gap:
                comparisons += 1
                if (temp < nums[j - gap]): #looks like we're starting at pos at least equal to gap. nums[j-gap] is nums[5-5] so nums[0]
                    nums[j] = nums[j - gap]
                    j -= gap #now check with j lower i guess?
                else:
                    break
            nums[j] = temp
    return comparisons


def shell_sort_gapped_descending(nums: list[int], gap, n):
    comparisons = 0
    for i in range (gap, n, 1): 
            temp = nums[i] 
            j = i 
            while j >= gap:
                comparisons += 1
                if (temp > nums[j - gap]): #looks like we're starting at pos at least equal to gap. nums[j-gap] is nums[5-5] so nums[0]
                    nums[j] = nums[j - gap]
                    j -= gap #now check with j lower i guess?
                else:
                    break
            nums[j] = temp
    return comparisons

# x2 = [-502, 42, 895, 231, 90, 8694, -21203, -24, 596, 723, -911, -100, 5382, 420]
# x1 = [-502, 42, 895, 231, 90, 8694, -21203, -24, 596, 723, -911, -100, 5382, 420]
# x3 = [-502, 42, 895, 231, 90, 8694, -21203, -24, 596, 723, -911, -100, 5382, 420]
# x4 = [-502, 42, 895, 231, 90, 8694, -21203, -24, 596, 723, -911, -100, 5382, 420, -502, 42, 895, 231, 90, 8694, -21203, -24, 596, 723, -911, -100, 5382, 420, -502, 42, 895, 231, 90, 8694, -21203, -24, 596, 723, -911, -100, 5382, 420]
# print(x2)
# shell_sort2(x2)
# shell_sort1(x1)
# shell_sort3(x3)
# print(x2)
# print(x1)
# print(x3)
# shell_sort4(x4)

# x = [5, 2, 4, 1, 3, 11, 9, 8, 7, 6, 0, 10]
# print(f"shell_sort1 comparisons: {shell_sort1(x)}, x: {x}")
# x = [5, 2, 4, 1, 3, 11, 9, 8, 7, 6, 0, 10]
# print(f"shell_sort2 comparisons: {shell_sort2(x)}, x: {x}")
# x = [5, 2, 4, 1, 3, 11, 9, 8, 7, 6, 0, 10]
# print(f"shell_sort3 comparisons: {shell_sort3(x)}, x: {x}")
# x = [5, 2, 4, 1, 3, 11, 9, 8, 7, 6, 0, 10]
# print(f"shell_sort4 comparisons: {shell_sort4(x)}, x: {x}")
# x = [5, 2, 4, 1, 3, 11, 9, 8, 7, 6, 0, 10]
# print(f"shell_sort5 comparisons: {shell_sort5(x)}, x: {x}")
