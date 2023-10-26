from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]
def best_first_search(actual_Src, target, n):
	visited = [False] * n
	pq = PriorityQueue()
	pq.put((0, actual_Src))
	visited[actual_Src] = True
	while pq.empty() == False:
		u = pq.get()[1]
		print(u, end=" ")
		if u == target:
			break
		for v, c in graph[u]:
			if visited[v] == False:
				visited[v] = True
				pq.put((c, v))
	print()
# Function for adding edges to graph
def addedge(x, y, cost):
	graph[x].append((y, cost))
	graph[y].append((x, cost))
# The nodes shown in above example(by alphabets) are
# implemented using integers addedge(x,y,cost);
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)
source = 0
target = 9
best_first_search(source, target, v)


# Greedy best-first search algorithm always selects the path which appears best at that moment. 
# It is the combination of depth-first search and breadth-first search algorithms. 
# It uses the heuristic function and search. 
# Best-first search allows us to take the advantages of both algorithms. 
# With the help of best-first search, at each step, we can choose the most promising node. 
# In the best first search algorithm, we expand the node which is closest to the goal node and the closest cost is estimated by heuristic function, i.e.
# f(n)= g(n).   
# Were, h(n)= estimated cost from node n to the goal.
# The greedy best first algorithm is implemented by the priority queue.

# Best first search algorithm:
# Step 1: Place the starting node into the OPEN list.
# Step 2: If the OPEN list is empty, Stop and return failure.
# Step 3: Remove the node n, from the OPEN list which has the lowest value of h(n), 
# and places it in the CLOSED list.

# Step 4: Expand the node n, and generate the successors of node n.
# Step 5: Check each successor of node n, and find whether any node is a goal node or not. 
# If any successor node is goal node, then return success and terminate the search, 
# else proceed to Step 6.

# Step 6: For each successor node, algorithm checks for evaluation function f(n), 
# and then check if the node has been in either OPEN or CLOSED list. 
# If the node has not been in both list, then add it to the OPEN list.

# Step 7: Return to Step 2.