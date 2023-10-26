import math
class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

def get_gcd(x, y):
    if y == 0:
        return x
    return get_gcd(y, x % y)

def pour_water(from_capacity, to_capacity, d):
    from_cap = from_capacity
    to_cap = 0
    req_step = 1

    while from_cap != d and to_cap != d:
        max_pour = min(from_cap, to_capacity - to_cap)

        to_cap = to_cap + max_pour
        from_cap = from_cap - max_pour
        req_step += 1

        if from_cap == d or to_cap == d:
            break

        if from_cap == 0:
            from_cap = from_capacity
            req_step += 1

        if to_cap == to_capacity:
            to_cap = 0
            req_step += 1

    return req_step

def find_min_steps(i, j, d):
    if i > j:
        i, j = j, i

    if d > j:
        return -1

    if d % get_gcd(j, i) != 0:
        return -1

    return min(pour_water(j, i, d), pour_water(i, j, d))

def find_path(i, j, d):
    path = []
    from_cap = i
    to_cap = 0

    while from_cap != d and to_cap != d:
        max_pour = min(from_cap, j - to_cap)
        to_cap = to_cap + max_pour
        from_cap = from_cap - max_pour
        path.append(State(from_cap, to_cap))

        if from_cap == d or to_cap == d:
            break

        if from_cap == 0:
            from_cap = i

        if to_cap == j:
            to_cap = 0

    path.append(State(from_cap, to_cap))
    return path

if __name__ == "__main__":
    i = int(input("Enter the size of Jug1 in liters: "))
    j = int(input("Enter the size of Jug2 in liters: "))
    d = int(input("Enter the amount of water you want to measure: "))

    min_steps = find_min_steps(i, j, d)
    if min_steps == -1:
        print(f"Cannot measure {d} liters with jug capacities {i} and {j}.")
    else:
        print(f"Minimum number of steps required to measure water is {min_steps}")
        path = find_path(i, j, d)
        print("Path of states:")
        for state in path:
            print(f"Jug1: {state.jug1} liters, Jug2: {state.jug2} liters")





# You are on the side of the river. You are given  
# a m liter jug and a n liter jug where 0 < m < n. Both the jugs are initially empty.  
# The jugs don’t have markings to allow measuring smaller quantities. 
# You have to use the jugs to measure d liters of water where d < n.  
# Determine the minimum no of operations to be performed to obtain d liters of water in one of jug.  
# The operations you can perform are:  
# 1.	Empty a Jug 
# 2.	Fill a Jug 
# 3.	Pour water from one jug to the other until one of the jugs is either empty or full. 
 
# There are several ways of solving this problem including BFS and DP. 
# In this article, an arithmetic approach to solving the problem is discussed. 
# The problem can be modeled by means of the Diophantine equation of the form mx + ny = d which is solvable 
# if and only if gcd(m, n) divides d. 
# Also, the solution x,y for which equation is satisfied can be given using the Extended Euclid algorithm for GCD.  

# For example, if we have a jug J1 of 5 liters (n = 5) and another jug J2 of 3 liters (m = 3) 
# and we have to measure 1 liter of water using them.  
# The associated equation will be 5n + 3m = 1.  
# First of all this problem can be solved since gcd(3,5) = 1 which divides 1. 
# Using the Extended Euclid algorithm, we get values of n and m for which the equation is satisfied 
# which are n = 2 and m = -3. 

# Now to find the minimum no of operations to be performed we must decide which jug should be 
# filled first. Depending upon which jug is chosen to be filled and 
# which to be emptied we have two different solutions and the minimum among them would be our answer. 
# Solution 1 (Always pour from m liter jug into n liter jug)  
# 4.	Fill the m litre jug and empty it into n liter jug. 
# 5.	Whenever the m liter jug becomes empty fill it. 
# 6.	Whenever the n liter jug becomes full empty it. 
# 7.	Repeat steps 1,2,3 till either n liter jug or the m liter jug contains d litres of water. 
# Each of steps 1, 2 and 3 are counted as one operation that we perform. 
# Let us say algorithm 1 achieves the task in C1 no of operations. 

# Solution 2 (Always pour from n liter jug into m liter jug)   
# 8.	Fill the n liter jug and empty it into m liter jug. 
# 9.	Whenever the n liter jug becomes empty fill it. 
# 10.	Whenever the m liter jug becomes full empty it. 
# 11.	Repeat steps 1, 2 and 3 till either n liter jug or the m liter jug contains d liters of water. 
