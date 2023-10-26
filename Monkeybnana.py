def move(state, action):
    if action == "grasp":
        return ("holding", state[1])
    elif action == "climb":
        return ("onbox", state[1])
    elif action == "drag":
        return ("onfloor", state[1])
    elif action == "walk":
        return ("onfloor", state[1])

def can_get(state):
    return state[0] == "holding"

def solve_puzzle():
    initial_state = ("climb", "B")
    actions = ["grasp", "climb", "drag", "walk"]
    
    for action in actions:
        new_state = move(initial_state, action)
        if can_get(new_state):
            return True
    return False

initial_state = ("climb", "B")
if can_get(initial_state):
    print("The puzzle can be solved.")
else:
    if solve_puzzle():
        print("The puzzle can be solved.")
    else:
        print("The puzzle cannot be solved.")




# So how can the monkey get the bananas?
# So if the monkey is clever enough, he can come to the block, drag the block to the center, 
# climb on it, and get the banana. Below are few observations in this case −

# 1 Monkey can reach the block, if both of them are at the same level.

# 2 If the block position is not at the center, then monkey can drag it to the center.

# 3 If monkey and the block both are on the floor, and block is at the center, 
# then the monkey can climb up on the block. So the vertical position of the monkey will be changed.

# 4 When the monkey is on the block, and block is at the center, then the monkey can get the bananas.

# Now, let us see how we can solve this using Prolog. We will create some predicates as follows −

# 1 We have some predicates that will move from one state to another state, by performing action.

# 2 When the block is at the middle, and monkey is on top of the block, 
# and monkey does not have the banana (i.e. has not state), then using the grasp action, 
# it will change from has not state to have state.

# 3 From the floor, it can move to the top of the block (i.e. on top state), by performing the action climb.

# 4 The push or drag operation moves the block from one place to another.

# 5 Monkey can move from one place to another using walk or move clauses.