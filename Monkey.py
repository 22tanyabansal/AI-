class State:
    def __init__(self, monkey_x, monkey_y, box_x, box_y, has_box):
        self.monkey_x = monkey_x
        self.monkey_y = monkey_y
        self.box_x = box_x
        self.box_y = box_y
        self.has_box = has_box

    def __eq__(self, other):
        return self.monkey_x == other.monkey_x and self.monkey_y == other.monkey_y \
            and self.box_x == other.box_x and self.box_y == other.box_y and self.has_box == other.has_box

    def __hash__(self):
        return hash((self.monkey_x, self.monkey_y, self.box_x, self.box_y, self.has_box))

def actions(state):
    possible_actions = []
    if state.monkey_x < state.box_x:
        possible_actions.append("Move Right")
    elif state.monkey_x > state.box_x:
        possible_actions.append("Move Left")
    if state.monkey_y < state.box_y:
        possible_actions.append("Move Down")
    elif state.monkey_y > state.box_y:
        possible_actions.append("Move Up")
    if state.monkey_x == state.box_x and state.monkey_y == state.box_y and not state.has_box:
        possible_actions.append("Climb Box")
    return possible_actions

def monkey_banana_problem():
    start_state = State(1, 1, 2, 2, False)
    goal_state = State(2, 2, 2, 2, True)
    
    visited = set()
    stack = [(start_state, [])]
    
    while stack:
        current_state, path = stack.pop()
        
        if current_state == goal_state:
            return path
        
        visited.add(current_state)
        
        for action in actions(current_state):
            new_state = apply_action(current_state, action)
            if new_state not in visited:
                new_path = path + [action]
                stack.append((new_state, new_path))
    
    return None

def apply_action(state, action):
    if action == "Move Right":
        return State(state.monkey_x + 1, state.monkey_y, state.box_x, state.box_y, state.has_box)
    elif action == "Move Left":
        return State(state.monkey_x - 1, state.monkey_y, state.box_x, state.box_y, state.has_box)
    elif action == "Move Down":
        return State(state.monkey_x, state.monkey_y + 1, state.box_x, state.box_y, state.has_box)
    elif action == "Move Up":
        return State(state.monkey_x, state.monkey_y - 1, state.box_x, state.box_y, state.has_box)
    elif action == "Climb Box":
        return State(state.monkey_x, state.monkey_y, state.box_x, state.box_y, True)

path = monkey_banana_problem()

if path:
    print("Path to the banana:")
    for step in path:
        print(step)
else:
    print("No path found.")




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