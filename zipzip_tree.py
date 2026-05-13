# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file
# Explanations for ZipZipTree public member functions:

import random
import math
from functools import total_ordering

#from __future__ import annotations

from typing import TypeVar
from dataclasses import dataclass


# any variable annotated with KeyType should use the same type for each tree, and should be comparable.
KeyType = TypeVar('KeyType')

# ValType is for any additional data to be stored in the nodes.
ValType = TypeVar('ValType')

@dataclass
# Rank is a container representing each node's rank, both geometric and uniform.
#           If using an earlier form of Python, you can use a named tuple instead.

@total_ordering
class Rank:
	geometric_rank = 0
	uniform_rank = 0
	def __init__(self, geo = 0, uni = 0):
		self.geometric_rank = geo
		self.uniform_rank = uni


	def __eq__(self, other):
		if(other == None):
			return False
		return self.geometric_rank == other.geometric_rank and self.uniform_rank == other.uniform_rank
	
	
	def __lt__(self, other):
		if other is None:
			return False
		if self.geometric_rank == other.geometric_rank:
			return self.uniform_rank < other.uniform_rank
		return self.geometric_rank < other.geometric_rank
	
	# def __gt__(self, other):
	# 	if (self.geometric_rank > other.geometric_rank):
	# 		return True
	# 	elif self.geometric_rank == other.geometric_rank:
	# 		return self.uniform_rank > other.uniform_rank
	# 	else:
	# 		return False
		
	# def __lt__(self, other):
	# 	if (self.geometric_rank < other.geometric_rank):
	# 		return True
	# 	elif self.geometric_rank == other.geometric_rank:
	# 		return self.uniform_rank < other.uniform_rank
	# 	else:
	# 		return False
	
	# def __ge__(self, other):
	# 	return self > other or self == other
	
	# def __le__(self, other):
	# 	return self < other or self == other

@total_ordering

class Node:
	rank: Rank #this determines the node's height in the tree. if we're both geo rank 3, but i have a higher uniform
	#rank, then you become my child. (left if your val is smaller, right if not). if you're rank geo 2 and im 3,
	#again you become my child.

	#We’ll store the rank, 
	# the remaining capacity of the specific node, 
	# and the largest capacity of the whole subtree rooted at that node. 
	key: KeyType #bin index
	val: ValType #remaining capacity?

	#so if the tree is sorted by bin indexes as the key ("The ordering of the tree is by bin index."), then
	#how do i quickly traverse to find the best fit/first fit? ahhh
	#best fit: storing bins by order by remaining capacity as search key
	#first fit: ordering of the tree is by bin index
	def __init__(self, key: KeyType, val: ValType, rank: Rank, brc):
		self.key = key #this is the bin index
		self.val = val #remaining size of the bin? so this needs to be reduced and updated when more is added to the tree...
		self.brc = brc #must be updated once placed in tree...
		self.rank = rank
		self.left = None
		self.right = None
	def __str__(self):
		return (f"geom: {self.rank.geometric_rank}, unif: {self.rank.uniform_rank}, key: {self.key}, left: {self.left if self.left == None else self.left.key}, right: {self.right if self.right == None else self.right.key}, val: {self.val}, brc: {self.brc} ")
	
	def __eq__(self, other):
		if(other == None):
			return False
		return self.rank == other.rank and self.key == other.key
	
	def __lt__(self, other):
		if(other == None):
			return False
		
		if self.rank == other.rank:
			return self.key > other.key
		
		return self.rank < other.rank
		

	
	
def get_priority(node1: Node, node2: Node):
	if node1.rank < node2.rank:
		return False
	
	if node1.rank > node2.rank:
		return True
	
	return node1.key < node2.key


class ZipZipTree:
# ZipZipTree(): constructs the zip-zip tree with a specific capacity.
	capacity: int #how many items are in the list of data. worst case is we use the full capacity
	#nodes: list[Node]
	root: Node
	def __init__(self, capacity: int):
		self.capacity = capacity
		#self.nodes = []
		self.root = None
		#self.get_random_rank()
		#root = None
# get_random_rank(): returns a random node rank, chosen independently from:

	def get_random_rank(self) -> Rank:
		rank = Rank()
		#a geometric distribution of mean 1 and,

		while(random.randint(1,2) % 2 == 1):
			#print("in geometric rank")
			rank.geometric_rank += 1
		#a uniform distribution of integers from 0 to log(capacity)^3 - 1 (log capacity cubed minus 1).
		rank.uniform_rank = random.randint(0, int(math.log(self.capacity)**3)-1)
		return rank
# insert(): inserts item with parameter key, value, and rank into tree.
#           if rank is not provided, a random rank should be selected by using get_random_rank().

	def insert(self, key: KeyType, val: ValType, rank = None, brc = None):
		brc_list = []
		if (rank == None):
			rank = self.get_random_rank()
		x = Node(key, val, rank, brc)
		#self.nodes.append(newNode)
		curr = self.root
		prev = None
		#x = len(self.nodes)-1
		#go through current until rank >= current's rank (once we find where rank is bigger, we know where to put it)
		# or rank != current's rank and key <= current key (in the very rare chance ranks are equal, use key as a comparison)
		while curr != None and (rank < curr.rank or (rank == curr.rank and key > curr.key)):
			brc_list.append(curr)
			prev = curr #we're gonna change current, so save previous
			if (key < curr.key): #rank isn't bigger, so traverse using key.
				curr = curr.left #look left if our key is smaller than current's
			else:
				curr = curr.right #else look right.

		#placing x in the tree...
		if (curr == self.root): #if current is the root, we need to make our newNode the new root.
			self.root = x #this could be because it's null or x had a bigger rank, or tied rank and bigger val.
		elif(key < prev.key): #else current is the root, but our key is smaller than the parent,
			prev.left = x #then replace left with x
		else: #else it's bigger or equal
			prev.right = x #so replace x with right
		
		#set curr to become one of x's children	
		#if current did end up exiting because it was null, we were at the bottom, so we can return.
		if curr == None:
			#self.set_subtree_brc(self.root)
			#print(f'brc list 0 is {brc_list[0]}')
			if len(brc_list) != 0:
				self.set_brc_list(brc_list)
			return x
		#however, if we weren't at the bottom, we have to replace the subtree at curr
		if key < curr.key: #if our key is less than the key we're replacing
			x.right = curr #place that current on the right
		else:
			x.left = curr #otherwise, place that current on the left
		prev = x #now we have to track starting from our new key.

		#curr still equals the node x replaced...
		while(curr != None): #do this until we hit the bottom
			fix = prev #we have to save this position to reference it later for a rebalance
			if curr.key < key: #if we replaced curr to be on x's left
				while(True): #we need to check current's right, because that will become x's right if it's greater than x.
					prev = curr #save our current
					brc_list.append(curr)
					curr = curr.right #set current to it's own right child
					if(curr == None or curr.key > key): #if curr greater than our key, we have to use it
						break #as x's new right, so break and jump down. 
			else:
				while(True):#same stuff but we were placed on x's right.
					prev = curr
					brc_list.append(curr)
					curr = curr.left #check current's left
					if(curr == None or curr.key < key):#if curr is less than our key, we have to use it
						break #as x's new left
			#fix is saved to x on first iteration, though multiple rebalances might need to happen.
											#if fix equals x, and parent of current is bigger
											#place the key on x's left.
											#this same process can repeat but for the parent.
			if fix.key > key or (fix == x and prev.key > key): #prev is the node x replaced and pushed down...
				fix.left = curr
				brc_list.append(fix)
			else:
				fix.right = curr
				brc_list.append(fix)
		#self.set_subtree_brc(x)
		#self.set_subtree_brc(self.root)
		#print(f'brc list len-1 is {brc_list[len(brc_list)-1]}, size is {len(brc_list)}')
		if len(brc_list) != 0:
			self.set_brc_list(brc_list)
		return x
		
# remove(): removes item with parameter key from tree.
#           you can assume that the item exists in the tree.
	def remove(self, key: KeyType):
		brc_list = []
		curr = self.root
		prev = None
		while key != curr.key: #search until we find the key
			prev = curr
			brc_list.append(curr)
			# if key == curr.key:
			# 	curr = self.find_val(curr, key, val)
			# 	break
			if key < curr.key:
				curr = curr.left
			else:
				curr = curr.right
		x = curr
		#we found it, now we save the left and right of what's being deleted.
		left = curr.left
		right = curr.right
		
		if left == None: #if there's no left, set current to it's right
			curr = right
		elif right == None: #if there's a left but no right, set curr to it's left
			curr = left
		elif left >= right: #if there's a left and a right, see who's rank is higher and set curr to that.
			curr = left
		else:
			curr = right

		#prev is the node just before the node to be deleted.
		#curr is the node to be put in it's place.
		#x = curr
		if self.root == x:
			self.root = curr
		elif key < prev.key:
			prev.left = curr #save the removed key's parent to be connected to left or right...
		else:
			prev.right = curr
		#brc_list.append(curr)
		#as of this point, left and right are still the removed nodes left and right
		while left != None and right != None: 
			if left >= right:
				while(True):
					prev = left
					brc_list.append(left)
					left = left.right
					if (left == None or left.rank < right.rank):
						break
				prev.right = right
			else:
				while(True):
					prev = right
					brc_list.append(right)
					right = right.left
					if (right == None or left.rank >= right.rank):
						break
				prev.left = left
		#self.set_subtree_brc(self.root)
		#self.set_subtree_brc(x)
		if len(brc_list) != 0:
			self.set_brc_list(brc_list)

# find(): returns the value of item with parameter key.
#         you can assume that the item exists in the tree.
	def find_val(self, root: Node, key: KeyType, val: ValType):
		if root == None or root.key != key:
			return None
		if root.val == val:
			return root
		right = self.find_val(root.right, key, val)
		left = self.find_val(root.left, key, val)
		if right != None:
			return right
		elif left != None:
			return left
		return None
		
	def find(self, key: KeyType) -> ValType:
		curr = self.root
		while(curr != None and curr.key != key):
			if(curr.key < key):
				curr = curr.right
			else:
				curr = curr.left
		return curr.val
# get_size(): returns the number of nodes in the tree.

	def get_size(self) -> int:
		return self.count_subtree(0, self.root)
	
	def count_subtree(self, count, root):
		if root == None:
			return count
		count += 1
		count += self.count_subtree(0, root.left)
		count += self.count_subtree(0, root.right)
		return count


	def get_height(self) -> int:
		return self.calculate_height(self.root)
	
	def calculate_height(self, root):
		if root is None:
			return -1
		
		return 1 + max(self.calculate_height(root.left), self.calculate_height(root.right))


# get_depth(): returns the depth of the item with parameter key.
#              you can assume that the item exists in the tree.

	def get_depth(self, key: KeyType):
		curr = self.root
		depth = 0
		while(curr != None and curr.key != key):
			depth += 1
			if(curr.key < key):
				curr = curr.right
			else:
				curr = curr.left
		return depth


	def __str__(self):
		result = []
		self.strBFS(self.root, 0, result)
		printout = ""
		for level in result:
			printout += (' '.join(map(str, level)))
			printout += "\n"
		# for i in range(0, len(result)):
		# 	printout += str(result[i][0])#(f"{result[i]}, ")
		# 	printout += "\n"
		return printout

	def strDFS(self, rt: Node) -> str:
		printout: str
		printout = ""
		if rt != None:
			printout += self.strDFS(rt.left)

			printout += (f"{rt.key}, ")

			printout += self.strDFS(rt.right)
		return printout
	
	def strBFS(self, rt: Node, level, result):
		if rt == None:
			return
		
		if len(result) <= level:
			result.append([])
		
		result[level].append(rt)

		self.strBFS(rt.left, level + 1, result)
		self.strBFS(rt.right, level + 1, result)


	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define

	def set_subtree_brc(self, root):
		if root == None:
			return
		self.set_subtree_brc(root.left)
		self.set_subtree_brc(root.right)
		root.brc = max(root.val if root.val != None else 0, root.left.brc if root.left != None else 0, root.right.brc if root.right != None else 0)

	def set_brc_list(self, brc_list):
		#for i in range(len(brc_list)-1, -1, -1):
		for node in reversed(brc_list):
			if(node.brc == None):
				return
			#print(f'node {node} in brc_list')
	
			node.brc = max(node.val, node.left.brc if (node.left != None and node.left.brc != None) else 0.0, node.right.brc if node.right != None and node.right.brc != None else 0.0)
		#print("end set brc list")

	def find_best_fit(self, key: KeyType, free_space: list[float]):
		#find the smallest item bigger or equal to key...
		#if key is bigger, then avoid it...
		#if key is smaller... then what?
		curr = self.root
		candidate = None
		
		while(curr != None):
			if(curr.key[0] < key):
				curr = curr.right #the current node is too small to fit the key, leave candidate untouched and look right...
			elif(curr.key == key):
				candidate = curr
				break
			else:
				candidate = curr #candidate can now equal curr because it's greater than or equal to key.
				#if free_space[candidate.val] < 0:
					#print(f"candidate key:{candidate.key}, freespace[cand.val]: {free_space[candidate.val]}")
				curr = curr.left #look left for a better fit
		#so long as candidate doesn't equal None, we found a viable candidate
		index = None
		if candidate == None:
			free_space.append(1.0-key)
			index = len(free_space)-1
			free_space[index] = round(free_space[index], 8)
			self.insert([free_space[index],index], index, None, None)
		else:
			index = candidate.val
			self.remove(candidate.key)
			free_space[index] -= key
			free_space[index] = round(free_space[index], 8)
			if (free_space[index]) > 0:
				self.insert([free_space[index],index], index, None, None) ##reinsert node with updated capactiy and the same value
				
		#if no candidate, then insert
		

		return index

	#need an alg that finds left most node that fits fast
	def get_first_fit(self, val: ValType) -> int:
		brc_list = []
		curr = self.root
		if(curr == None):
			#print(f"curr is none at value {val}")
			return
		#print(self.root.brc)
		#print(curr)
		#we want LEFT MOST node that can fit the thing, so we only go right once we're out of lefts.
		#how do we know we're leftmost and can fit?
		#first check if left exists
			#then check if left's brc >= item
				#if yes to both, set curr to left and repeat process
		while(curr != None):
			brc_list.append(curr)
			#print(f"curr node index is {curr.key}")
			if curr.left != None and curr.left.brc >= val:
				curr = curr.left
				#if no to either, and curr.val >= item, place it in this node.
			elif curr.val >= val:
				curr.val -= val
				curr.val = round(curr.val, 8)
				curr.brc = max(curr.val, curr.left.brc if curr.left != None else 0, curr.right.brc if curr.right != None else 0)
				#self.set_subtree_brc(self.root)
				#for node in brc_list:
				#	print(f'node in brc_list {node}')
				#print('end')
				self.set_brc_list(brc_list)
				return curr.key
			else: #else, the value must be at right. set curr to curr.right
				#print(f"setting to right: {curr.right}")
				curr = curr.right
				#print(curr)
		#print(f"exiting: curr is none for val: {val}")
		#print(self)
		#quit()
		
		
		
		#keep going left until the brc is bigger than value, then check prev right.
		
#zzt = ZipZipTree(30)

# zzt.insert(1, 2, None, 5)
# #print(zzt.root)
# print(zzt)
# zzt.insert(3, 4, None, 4)

# print(zzt)
# zzt.insert(5, 12, None, 12)

# print(zzt)
# zzt.insert(56, 5, None, 1)

# print(zzt)
# zzt.insert(22, 16, None, 19)

# print(zzt)
# zzt.insert(52, 23)
# zzt.insert(55, 14)
# zzt.insert(59, 19)
# zzt.insert(85, 1)
# zzt.insert(-115, 15)
# zzt.insert(442, 154)
# print(f"count: {zzt.get_size()}")

# print(zzt)
# print(zzt.find(56))
# print(zzt.find(56))
# print(zzt.find(56))
# height = zzt.get_height()
#print(height)


# zzt.remove(52)
# print(zzt)
# zzt.remove(22)
# print(zzt)
# zzt.remove(56)
# print(zzt)
# zzt.remove(5)
# print(zzt)
# zzt.remove(3)
# print(zzt)
# zzt.remove(1)
# print(zzt.root)
# print(zzt)



#for node in zzt.nodes:
#	print(node)