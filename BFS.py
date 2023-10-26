from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
if __name__ == '__main__':
	# Create a graph given in
	# the above diagram
	g = Graph()
	while True:
		a, b = map(int, input("Enter starting and ending vertices (-1, -1 to exit): ").split())
		if a == -1 and b == -1:
			break
		g.addEdge(a, b)

	print("Following is Breadth First Traversal"
		" (starting from vertex 2)")
	g.BFS(2)


# Breadth-first search is the most common search strategy for traversing a tree or graph. 
# This algorithm searches breadthwise in a tree or graph, so it is called breadth-first search.
# BFS algorithm starts searching from the root node of the tree and expands all successor node at the current level before moving to nodes of next level.
# The breadth-first search algorithm is an example of a general-graph search algorithm.
# Breadth-first search implemented using FIFO queue data structure.
# Rule 1 − Visit the adjacent unvisited vertex. Mark it as visited. Display it. Insert it in a queue.

# Rule 2 − If no adjacent vertex is found, remove the first vertex from the queue.

# Rule 3 − Repeat Rule 1 and Rule 2 until the queue is empty.
# Advantages:
# BFS will provide a solution if any solution exists.
# If there are more than one solutions for a given problem, then BFS will provide the minimal solution which requires the least number of steps.

# Disadvantages:
# It requires lots of memory since each level of the tree must be saved into memory to expand the next level.
# BFS needs lots of time if the solution is far away from the root node.