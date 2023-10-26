from collections import defaultdict
class Graph:
	def __init__(self,vertices):
		self.V = vertices
		self.graph = defaultdict(list)
	def addEdge(self,u,v):
		self.graph[u].append(v)
	def DLS(self,src,target,maxDepth):
		if src == target : return True
		# If reached the maximum depth, stop recursing.
		if maxDepth <= 0 : return False
		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[src]:
				if(self.DLS(i,target,maxDepth-1)):
					return True
		return False
	# IDDFS to search if target is reachable from v.
	# It uses recursive DLS()
	def IDDFS(self,src, target, maxDepth):
		# Repeatedly depth-limit search till the
		# maximum depth
		for i in range(maxDepth):
			if (self.DLS(src, target, i)):
				return True
		return False
# Create a graph given in the above diagram
g = Graph (7);
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)
target = 6; maxDepth = 3; src = 0
if g.IDDFS(src, target, maxDepth) == True:
	print ("Target is reachable from source " +
		"within max depth")
else :
	print ("Target is NOT reachable from source " +
		"within max depth")



# The iterative deepening algorithm is a combination of DFS and BFS algorithms. 
# This search algorithm finds out the best depth limit and does it by gradually 
# increasing the limit until a goal is found.
# This algorithm performs depth-first search up to a certain "depth limit", 
# and it keeps increasing the depth limit after each iteration until the goal node is found.
# This Search algorithm combines the benefits of Breadth-first search's 
# fast search and depth-first search's memory efficiency.
# The iterative search algorithm is useful uninformed search when search space is large, and depth of goal node is unknown.

# Advantages:
# Itcombines the benefits of BFS and DFS search algorithm in terms of fast search and memory efficiency.
# Disadvantages:
# The main drawback of IDDFS is that it repeats all the work of the previous phase.
