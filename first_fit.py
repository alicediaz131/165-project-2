# Example file: next_fit.py
from zipzip_tree import ZipZipTree
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

def first_fit(items: list[float], assignment: list[int], free_space: list[float]):
	tree = ZipZipTree(len(items))
	j = 0
	free_space.append(1.0)
	tree.insert(0, 1.0)
	#tree.insert(0, 1.0)
	for i in range(0, len(items)):
		if(tree.root.brc < items[i]):
			#print(tree.root.brc)
			print("appending")
			free_space.append(1.0)
			tree.insert(len(free_space)-1, 1.0)
		ff_index = tree.get_first_fit(items[i])
		free_space[ff_index] -= items[i]
		assignment[i] = ff_index
		#free_space[j] -= items[i]

items = [0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4]
assignment = [0]*len(items)
free_space = []

first_fit(items, assignment, free_space)

print(items)
print(assignment)
print(free_space)
	#need an alg that checks left most subtree first
	#repeat the keep going left thing
	#we want LEFT MOST node that can fit the thing, so we only go right once we're out of lefts.
	#how do we know we're leftmost and can fit?
	#first check if left exists
		#then check if left's brc >= item
			#if yes to both, set curr to left and repeat process
	#if no to either, and curr.val >= item, place it in this node.
	#else, the value must be at right. set curr to curr.right
	
	#keep going left until the brc is bigger than value, then check prev right.
