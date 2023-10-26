def dfs(graph, source, path=[]):
    if source not in path:
        path.append(source)

    if source not in graph:
        return path

    for neighbor in graph[source]:
        path = dfs(graph, neighbor, path)
    return path

# Function to build a graph from user input
def build_graph():
    graph = {}
    while True:
        source = input("Enter a node (or press Enter to finish): ")
        if not source:
            break
        neighbors = input("Enter neighbors of {} (comma-separated): ".format(source)).split(',')
        graph[source] = [neighbor.strip() for neighbor in neighbors]
    return graph

# Get user input for the graph
print("Enter the graph (press Enter to finish input):")
user_graph = build_graph()

# Get the starting node from the user
starting_node = input("Enter the starting node: ")

# Perform DFS on the user-defined graph
dfs_element = dfs(user_graph, starting_node)
print("DFS result:", dfs_element)


# Depth-first search isa recursive algorithm for traversing a tree or graph data structure.
# It is called the depth-first search because it starts from the root node and 
# follows each path to its greatest depth node before moving to the next path.
# DFS uses a stack data structure for its implementation.
# The process of the DFS algorithm is similar to the BFS algorithm.
# Advantage:
# DFS requires very less memory as it only needs to store a stack of the nodes 
# on the path from root node to the current node.
# It takes less time to reach to the goal node than 
# BFS algorithm (if it traverses in the right path).

# Disadvantage:
# There is the possibility that many states keep re-occurring, 
# and there is no guarantee of finding the solution.
# DFS algorithm goes for deep down searching and sometime it may go to the infinite loop.