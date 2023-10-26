# Cost to find the AND and OR path
def Cost(H, condition, weight = 1):
	cost = {}
	if 'AND' in condition:
		AND_nodes = condition['AND']
		Path_A = ' AND '.join(AND_nodes)
		PathA = sum(H[node]+weight for node in AND_nodes)
		cost[Path_A] = PathA

	if 'OR' in condition:
		OR_nodes = condition['OR']
		Path_B =' OR '.join(OR_nodes)
		PathB = min(H[node]+weight for node in OR_nodes)
		cost[Path_B] = PathB
	return cost

# Update the cost
def update_cost(H, Conditions, weight=1):
	Main_nodes = list(Conditions.keys())
	Main_nodes.reverse()
	least_cost= {}
	for key in Main_nodes:
		condition = Conditions[key]
		print(key,':', Conditions[key],'>>>', Cost(H, condition, weight))
		c = Cost(H, condition, weight) 
		H[key] = min(c.values())
		least_cost[key] = Cost(H, condition, weight)		 
	return least_cost

# Print the shortest path
def shortest_path(Start,Updated_cost, H):
	Path = Start
	if Start in Updated_cost.keys():
		Min_cost = min(Updated_cost[Start].values())
		key = list(Updated_cost[Start].keys())
		values = list(Updated_cost[Start].values())
		Index = values.index(Min_cost)
		# FIND MINIMIMUM PATH KEY
		Next = key[Index].split()
		# ADD TO PATH FOR OR PATH
		if len(Next) == 1:
			Start =Next[0]
			Path += '<--' +shortest_path(Start, Updated_cost, H)
		# ADD TO PATH FOR AND PATH
		else:
			Path +='<--('+key[Index]+') '
			Start = Next[0]
			Path += '[' +shortest_path(Start, Updated_cost, H) + ' + '
			Start = Next[-1]
			Path += shortest_path(Start, Updated_cost, H) + ']'
	return Path
H = {'A': -1, 'B': 5, 'C': 2, 'D': 4, 'E': 7, 'F': 9, 'G': 3, 'H': 0, 'I':0, 'J':0}
Conditions = {
'A': {'OR': ['B'], 'AND': ['C', 'D']},
'B': {'OR': ['E', 'F']},
'C': {'OR': ['G'], 'AND': ['H', 'I']},
'D': {'OR': ['J']}
}
# weight
weight = 1
# Updated cost
print('Updated Cost :')
Updated_cost = update_cost(H, Conditions, weight=1)
print('*'*75)
print('Shortest Path :\n',shortest_path('A', Updated_cost,H))



# # The AO* method divides any given difficult problem into a smaller group of problems that are then resolved using the AND-OR graph concept. 
# AND OR graphs are specialized graphs that are used in problems that can be divided into smaller problems. 
# The AND side of the graph represents a set of tasks that must be completed to achieve the main goal, 
# while the OR side of the graph represents different methods for accomplishing the same main goal.
# The start state and the target state are already known in the knowledge-based search strategy known as the AO* algorithm, and the best path is identified by heuristics. 
# The informed search technique considerably reduces the algorithm’s time complexity. 
# The AO* algorithm is far more effective in searching AND-OR trees than the A* algorithm.
# Working of AO* algorithm:
# The evaluation function in AO* looks like this:
# f(n) = g(n) + h(n)
# f(n) = Actual cost + Estimated cost
# here,
#           f(n) = The actual cost of traversal.
#           g(n) = the cost from the initial node to the current node.
#           h(n) = estimated cost from the current node to the goal state.