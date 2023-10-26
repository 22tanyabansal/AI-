import copy
from heapq import heappush, heappop
n = 3
# bottom, left, top, right
row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]
class priorityQueue:
	def __init__(self):
		self.heap = []
	# Inserts a new key 'k'
	def push(self, k):
		heappush(self.heap, k)
	# Method to remove minimum element 
	# from Priority Queue
	def pop(self):
		return heappop(self.heap)
	# Method to know if the Queue is empty
	def empty(self):
		if not self.heap:
			return True
		else:
			return False

class node:
	def __init__(self, parent, mat, empty_tile_pos,
				cost, level):
		self.parent = parent
		# Stores the matrix
		self.mat = mat
		# Stores the position at which the
		# empty space tile exists in the matrix
		self.empty_tile_pos = empty_tile_pos
		# Stores the number of misplaced tiles
		self.cost = cost
		# Stores the number of moves so far
		self.level = level
	def __lt__(self, nxt):
		return self.cost < nxt.cost


def calculateCost(mat, final) -> int:
	count = 0
	for i in range(n):
		for j in range(n):
			if ((mat[i][j]) and
				(mat[i][j] != final[i][j])):
				count += 1		
	return count

def newNode(mat, empty_tile_pos, new_empty_tile_pos,
			level, parent, final) -> node:		
	# Copy data from parent matrix to current matrix
	new_mat = copy.deepcopy(mat)
	# Move tile by 1 position
	x1 = empty_tile_pos[0]
	y1 = empty_tile_pos[1]
	x2 = new_empty_tile_pos[0]
	y2 = new_empty_tile_pos[1]
	new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
	# Set number of misplaced tiles
	cost = calculateCost(new_mat, final)
	new_node = node(parent, new_mat, new_empty_tile_pos,
					cost, level)
	return new_node

# Function to print the N x N matrix
def printMatrix(mat):
	for i in range(n):
		for j in range(n):
			print("%d " % (mat[i][j]), end = " ")
			
		print()

# Function to check if (x, y) is a valid
# matrix coordinate
def isSafe(x, y):
	return x >= 0 and x < n and y >= 0 and y < n

# Print path from root node to destination node
def printPath(root):
	if root == None:
		return
	printPath(root.parent)
	printMatrix(root.mat)
	print()

# Function to solve N*N - 1 puzzle algorithm
# using Branch and Bound. empty_tile_pos is
# the blank tile position in the initial state.
def solve(initial, empty_tile_pos, final):
	pq = priorityQueue()
	# Create the root node
	cost = calculateCost(initial, final)
	root = node(None, initial, 
				empty_tile_pos, cost, 0)
	pq.push(root)
	while not pq.empty():
		minimum = pq.pop()
		# If minimum is the answer node
		if minimum.cost == 0:
			printPath(minimum)
			return
		# Generate all possible children
		for i in range(4):
			new_tile_pos = [
				minimum.empty_tile_pos[0] + row[i],
				minimum.empty_tile_pos[1] + col[i], ]			
			if isSafe(new_tile_pos[0], new_tile_pos[1]):
				# Create a child node
				child = newNode(minimum.mat,
								minimum.empty_tile_pos,
								new_tile_pos,
								minimum.level + 1,
								minimum, final,)
				# Add child to list of live nodes
				pq.push(child)
# Driver Code
# Initial configuration
# Value 0 is used for empty space
initial = [ [ 1, 2, 3 ], 
			[ 5, 6, 0 ], 
			[ 7, 8, 4 ] ]

# Solvable Final configuration
# Value 0 is used for empty space
final = [ [ 1, 2, 3 ], 
		[ 5, 8, 6 ], 
		[ 0, 7, 4 ] ]

# Blank tile coordinates in 
# initial configuration
empty_tile_pos = [ 1, 2 ]
# Function call to solve the puzzle
solve(initial, empty_tile_pos, final)

# A 3 by 3 board with 8 tiles (each tile has a number from 1 to 8) and a single empty space is 
# provided. 
# The goal is to use the vacant space to arrange the numbers on the tiles such that they match the 
# final arrangement. 
# Four neighbouring (left, right, above, and below) tiles can be moved into the available area.

# 1. DFS (Brute - Force) :
# On the state-space tree (Set of all configurations of a particular issue, i.e., 
# all states that may be reached from the beginning state), we can do a depth-first search.


# 2. BFS (Brute - Force) :
# We can search the state space tree using a breadth-first approach. 
# It always locates the goal state that is closest to the root. 
# However, the algorithm tries the same series of movements as DFS regardless of the initial state.

# 3. Branch and Bound :
# By avoiding searching in sub-trees which do not include an answer node, an "intelligent" ranking 
# function, also known as an approximatsion costs function, 
# may frequently speed up the search for an answer node. 
# Basically, Branch and Bound involves three different kinds of nodes.

# A live node is a created node whose children have not yet been formed.

# The offspring of the E-node which is a live node, are now being investigated. 
# Or to put it another way, an E-node is a node that is currently expanding.

# A created node which is not to be developed or examined further is referred to as a dead node. 
# A dead node has already extended all of its offspring.

# Final algorithm :
# In order to maintain the list of live nodes, algorithm LCSearch employs the functions Least() and Add().
# Least() identifies a live node with the least c(y), removes it from the list, and returns it.
# Add(y) adds y to the list of live nodes.
# Add(y) implements the list of live nodes as a min-heap.

