# Example file: next_fit.py
from zipzip_tree import ZipZipTree
from tim_sort import tim_sort
# explanations for member functions are provided in requirements.py

#For all bin packing functions:
# params:
# 	items: the items to assign to the bins
# 	assignment: the assignment of the ith item to the jth bin for all i items.
# 	            bin numbers start from 0.
# 	            assume len(assignment) == len(items).
# 	            you should not add any new elements to this list.
# 	            you must modify this list's elements to indicate the assignment.
# 	            see comment below for first-fit decreasing and for best-fit decreasing.
#
# 	free_space: the amount of space left in the jth bin for all j bins created by the algorithm.
# 	            you should add one element for each bin that the algorithm creates.
# 	            when the function returns, this should indicate the final free space available in each bin.

# For first-fit decreasing and best-fit decreasing:
# The assignment list argument should refer to item indices *after* sorting.
# You don't need to map the assignment indices in some clever way.
# As such, the assignments list for these algorithms will have little practical usage other than testing.


	#best fit: storing bins by order by remaining capacity as search key

def best_fit(items: list[float], assignment: list[int], free_space: list[float]):
	tree = ZipZipTree(len(items))
	#free_space.append(1.0)
	#tree.insert(1.0, 0)

	for i in range(0, len(items)):
		assignment[i] = tree.find_best_fit(items[i], free_space)
	#print(tree)


def best_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
	tim_sort(items)
	#print(items)
	best_fit(items, assignment, free_space)

# items = [0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4, 0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4,0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4
# 		,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2]
# assignment = [0]*len(items)
# free_space = []

# best_fit(items, assignment, free_space)

# print(items)
# print(assignment)
# print(free_space)


# items2 = [0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4]
# shell_sort6(items2)
# print(items2)
# assignment2 = [0]*len(items)
# free_space2 = []

# best_fit_decreasing(items2, assignment2, free_space2)

#print(items2)
#print(assignment2)
#print(free_space2)