from sys import maxsize 
from itertools import permutations
V = 4
# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 
	# store all vertex apart from source vertex 
	vertex = [] 
	for i in range(V): 
		if i != s: 
			vertex.append(i) 
	# store minimum weight Hamiltonian Cycle 
	min_path = maxsize 
	next_permutation=permutations(vertex)
	for i in next_permutation:
		# store current Path weight(cost) 
		current_pathweight = 0
		# compute current path weight 
		k = s 
		for j in i: 
			current_pathweight += graph[k][j] 
			k = j 
		current_pathweight += graph[k][s] 
		# update minimum 
		min_path = min(min_path, current_pathweight) 	
	return min_path 


# Driver Code 
if __name__ == "__main__": 
	# matrix representation of graph 
	graph = [[0, 10, 15, 20], [10, 0, 35, 25], 
			[15, 35, 0, 30], [20, 25, 30, 0]] 
	s = 0
	print(travellingSalesmanProblem(graph, s))


# Travelling Salesman Problem (TSP) : Given a set of cities and distances between every pair of cities, 
# the problem is to find the shortest possible route that visits every 
# city exactly once and returns to the starting point. 

# Note the difference between Hamiltonian Cycle and TSP. 
# The Hamiltonian cycle problem is to find if there exists a tour that visits every city exactly once. 
# Here we know that Hamiltonian Tour exists (because the graph is complete) and in fact, many such tours exist, 
# the problem is to find a minimum weight Hamiltonian Cycle. 


# In this post, the implementation of a simple solution is discussed.

# Consider city 1 as the starting and ending point. Since the route is cyclic, we can consider any point as a starting point.
# Generate all (n-1)! permutations of cities.
# Calculate the cost of every permutation and keep track of the minimum cost permutation.
# Return the permutation with minimum cost.


# Algorithm
# Travelling salesman problem takes a graph G {V, E} as an input and declare another graph as the output (say G’) which will record the path the salesman is going to take from one node to another.

# The algorithm begins by sorting all the edges in the input graph G from the least distance to the largest distance.

# The first edge selected is the edge with least distance, and one of the two vertices (say A and B) being the origin node (say A).

# Then among the adjacent edges of the node other than the origin node (B), find the least cost edge and add it onto the output graph.

# Continue the process with further nodes making sure there are no cycles in the output graph and the path reaches back to the origin node A.

# However, if the origin is mentioned in the given problem, then the solution must always start from that node only. Let us look at some example problems to understand this better.