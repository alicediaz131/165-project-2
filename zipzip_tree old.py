# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file
# Explanations for ZipZipTree public member functions:

import random
import math

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

class Rank:
	geometric_rank = 0
	uniform_rank = 0
	def __init__(self):
		self.geometric_rank = 0
		self.uniform_rank = 0

	def __eq__(self, other):
		return self.geometric_rank == other.geometric_rank and self.uniform_rank == other.uniform_rank
	
	def __ne__(self, other):
		return self.geometric_rank != other.geometric_rank and self.uniform_rank != other.uniform_rank
	
	def __gt__(self, other):
		if (self.geometric_rank > other.geometric_rank):
			return True
		elif self.geometric_rank == other.geometric_rank:
			return self.uniform_rank > other.uniform_rank
		else:
			return False
		
	def __lt__(self, other):
		if (self.geometric_rank < other.geometric_rank):
			return True
		elif self.geometric_rank == other.geometric_rank:
			return self.uniform_rank < other.uniform_rank
		else:
			return False
	
	def __ge__(self, other):
		return self > other or self == other
	
	def __le__(self, other):
		return self < other or self == other



class Node:
	rank: Rank #this determines the node's height in the tree. if we're both geo rank 3, but i have a higher uniform
	#rank, then you become my child. (left if your val is smaller, right if not). if you're rank geo 2 and im 3,
	#again you become my child.

	#We’ll store the rank, 
	# the remaining capacity of the specific node, 
	# and the largest capacity of the whole subtree rooted at that node. 
	key: KeyType #remaining capacity
	val: ValType #how much is stored of the whole subtree rooted at the node
	left: int
	right: int
	def __init__(self, key: KeyType, val: ValType, rank: Rank):
		self.key = key
		self.val = val
		self.rank = rank
		self.left = None
		self.right = None
	def __str__(self):
		return (f"geom: {self.rank.geometric_rank}, unif: {self.rank.uniform_rank}, key: {self.key}, left: {self.left}, right: {self.right}, val: {self.val}, ")

class ZipZipTree:
# ZipZipTree(): constructs the zip-zip tree with a specific capacity.
	capacity: int #how many items are in the list of data. worst case is we use the full capacity
	nodes: list[Node]
	root: int
	def __init__(self, capacity: int):
		self.capacity = capacity
		self.nodes = []
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

	def insert(self, key: KeyType, val: ValType, rank: Rank = None):
		if (rank == None):
			rank = self.get_random_rank()
		newNode = Node(key, val, rank)
		self.nodes.append(newNode)
		curr = self.root
		prev = None
		x = len(self.nodes)-1
		#go through current until rank >= current's rank (once we find where rank is bigger, we know where to put it)
		# or rank != current's rank and key <= current key (in the very rare chance ranks are equal, use key as a comparison)
		while curr != None and (rank < self.nodes[curr].rank or (rank == self.nodes[curr].rank and key > self.nodes[curr].key)):
			prev = curr #we're gonna change current, so save previous
			if (key < self.nodes[curr].key): #rank isn't bigger, so traverse using key.
				curr = self.nodes[curr].left #look left if our key is smaller than current's
			else:
				curr = self.nodes[curr].right #else look right.

		if (curr == self.root): #if current is the root, we need to make our newNode the new root.
			self.root = x #this could be because it's null or x had a bigger rank, or tied rank and bigger val.
			#print(f"root == {x}")
		elif(key < self.nodes[prev].key): #else current is the root, but our key is smaller than the parent,
			self.nodes[prev].left = x #then replace left with x
		else: #else it's bigger or equal
			self.nodes[prev].right = x #so replace x with right
		
		#if current did end up exiting because it was null, we were at the bottom, so we can return.
		if curr == None:
			return
		#however, if we weren't at the bottom, we have to replace the subtree at curr
		if key < self.nodes[curr].key: #if our key is less than the key we're replacing
			self.nodes[x].right = curr #place that current on the right
		else:
			self.nodes[x].left = curr #otherwise, place that current on the left
		prev = x #now we have to track starting from our new key.

		while(curr != None): #do this until we hit the bottom
			fix = prev #we have to save this position to reference it later for a rebalance
			if self.nodes[curr].key < key: #if we replaced curr to be on x's left
				while(True): #we need to check current's right, because that will become x's right if it's greater than x.
					prev = curr #save our current
					curr = self.nodes[curr].right #set current to it's own right child
					if(curr == None or self.nodes[curr].key > key): #if curr greater than our key, we have to use it
						break #as x's new right, so break and jump down.
			else:
				while(True):#same stuff but we were placed on x's right.
					prev = curr
					curr = self.nodes[curr].left #check current's left
					if(curr == None or self.nodes[curr].key < key):#if curr is less than our key, we have to use it
						break #as x's new left
			#fix is saved to x on first iteration, though multiple rebalances might need to happen.
											#if fix equals x, and parent of current is bigger
											#place the key on x's left.
											#this same process can repeat but for the parent.
			if self.nodes[fix].key > key or (fix == x and self.nodes[prev].key > key):
				self.nodes[fix].left = curr
			else:
				self.nodes[fix].right = curr
		
# remove(): removes item with parameter key from tree.
#           you can assume that the item exists in the tree.
	def remove(self, key: KeyType):
		curr = self.root
		prev = None
		while key != self.nodes[curr].key:
			prev = curr
			if key < self.nodes[curr].key:
				curr = self.nodes[curr].left
			else:
				curr = self.nodes[curr].right
		left = self.nodes[curr].left
		right = self.nodes[curr].right
		
		if left == None:
			curr = right
		elif right == None:
			curr = left
		elif self.nodes[left].rank >= self.nodes[right].rank:
			curr = left
		else:
			curr = right

		if self.nodes[self.root].key == key:
			self.root = curr
		elif key < self.nodes[prev].key:
			self.nodes[prev].left = curr
		else:
			self.nodes[prev].right = curr

		while left != None and right != None:
			if self.nodes[left].rank >= self.nodes[right].rank:
				while(True):
					prev = left
					left = self.nodes[left].right
					if (left == None or self.nodes[left].rank < self.nodes[right].rank):
						break
				self.nodes[prev].right = right
			else:
				while(True):
					prev = right
					right = self.nodes[right].left
					if (right == None or self.nodes[left].rank >= self.nodes[right].rank):
						break
				self.nodes[prev].left = left

# find(): returns the value of item with parameter key.
#         you can assume that the item exists in the tree.

	def find(self, key: KeyType) -> ValType:
		curr = self.root
		while(curr != None and self.nodes[curr].key != key):
			if(self.nodes[curr].key < key):
				curr = self.nodes[curr].right
			else:
				curr = self.nodes[curr].left
		return self.nodes[curr].val
# get_size(): returns the number of nodes in the tree.

	def get_size(self) -> int:
		pass
# get_height(): returns the height of the tree.

	def get_height(self) -> int:
		pass
# get_depth(): returns the depth of the item with parameter key.
#              you can assume that the item exists in the tree.

	def get_depth(self, key: KeyType):
		pass

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

	def strDFS(self, rt: int) -> str:
		printout: str
		printout = ""
		if rt != None:
			printout += self.strDFS(self.nodes[rt].left)

			printout += (f"{self.nodes[rt].key}, ")

			printout += self.strDFS(self.nodes[rt].right)
		return printout
	
	def strBFS(self, rt: int, level, result):
		if rt == None:
			return
		
		if len(result) <= level:
			result.append([])
		
		result[level].append(self.nodes[rt])

		self.strBFS(self.nodes[rt].left, level + 1, result)
		self.strBFS(self.nodes[rt].right, level + 1, result)


	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define


zzt = ZipZipTree(30)

zzt.insert(1, 2)
print(zzt.root)
print(zzt)
zzt.insert(3, 4)
print(zzt.root)
print(zzt)
zzt.insert(5, 12)
print(zzt.root)
print(zzt)
zzt.insert(56, 5)
print(zzt.root)
print(zzt)
zzt.insert(22, 16)
print(zzt.root)
print(zzt)
zzt.insert(52, 23)


print(zzt.root)
#print(zzt.nodes[0])
print(zzt)
print(zzt.find(56))
print(zzt.find(56))
print(zzt.find(56))


zzt.remove(52)
print(zzt)
zzt.remove(22)
print(zzt)
zzt.remove(56)
print(zzt)
zzt.remove(5)
print(zzt)
zzt.remove(3)
print(zzt)
zzt.remove(1)
print(zzt.root)
print(zzt)



for node in zzt.nodes:
	print(node)

