import copy
from queue import Queue

class Problem(object):

    def __init__(self, initial, goal=None):
        """This is the constructor for the Problem class. It specifies the initial state, and possibly a goal state, if there is a unique goal.  You can add other arguments if the need arises"""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        size = len(state)
        action_list = []
        column_list = make_column_list(state)
        box_list = make_box_list(state)
        only_option = False
        for x in range(0, size):
            for y in range(0, size):
                if state[x][y] == 0:
                    for z in range(1, size + 1):
                        if z not in state[x] and z not in column_list[y] and z not in box_list[which_box(size, x, y)]:
                            action_list.append([x, y, z, only_option])
        if action_list:
            for i in range(0, len(action_list)):
                if i == 0 and len(action_list) > 1:
                    if action_list[i][0] == action_list[i + 1][0] and action_list[i][1] == action_list[i + 1][1]:
                        action_list[i][3] = True
                elif i == len(action_list) - 1:
                    if action_list[i][0] == action_list[i - 1][0] and action_list[i][1] == action_list[i -1][1]:
                        action_list[i][3] = True
                elif (action_list[i][0] == action_list[i + 1][0] and action_list[i][1] == action_list[i + 1][1]) or (action_list[i][0] == action_list[i - 1][0] and action_list[i][1] == action_list[i -1][1]):
                    action_list[i][3] = True
        action_list = sorted(action_list, key = lambda x: x[3])
        return action_list
            
    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        if action[3] == False:
            state[action[0]][action[1]] = action[2]
            return state
        else:
            state_copy = copy.deepcopy(state)
            state_copy[action[0]][action[1]] = action[2]
            return state_copy

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal, as specified in the constructor. Override this
        method if checking against a single self.goal is not enough.
        This must be written by students"""
        size = len(state)
        goal_list = []
        for i in range(0, size):
            goal_list.append(list(range(1, size + 1)))
        row_list = copy.deepcopy(state)
        column_list = make_column_list(state)
        box_list = make_box_list(state)
        for x in range(0, size):
            row_list[x].sort()
            column_list[x].sort()
            box_list[x].sort()
        if goal_list == row_list == column_list == box_list:
            return True        
        else: return False
    

class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state"""

    def __init__(self, state, parent=None, action=None):
        """Create a search tree Node, derived from a parent by an action.
        Update the node parameters based on constructor values"""
        self.state = state
        self.parent = parent
        self.action = action
        # If depth is specified then depth of node will be 1 more than the depth of parent
        #if parent:
            #self.depth = parent.depth + 1

    def expand(self, problem):
        # List the nodes reachable in one step from this node.
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next = problem.result(self.state, action)
        return Node(next, self, action)
    

def breadth_first_search(problem):
    # Start from first node of the problem Tree
    node = Node(problem.initial)
    # Check if current node meets Goal_Test criteria
    if problem.goal_test(node.state):
        return node
    # Create a Queue to store all nodes of a particular level. Import QueueClass()
    frontier = Queue()
    frontier.put(node)
    # Loop until all nodes are explored(frontier queue is empty) or Goal_Test criteria are met
    while frontier.empty() == False:
        # Remove from frontier, for analysis
        node = frontier.get()
        # Loop over all children of the current node
        # Note: We consider the fact that a node can have multiple child nodes here
        for child in node.expand(problem):
            # If child node meets Goal_Test criteria
            if problem.goal_test(child.state):
                return child
            # Add every new child to the frontier
            frontier.put(child)
    return None

def sudoku_solver():
    again = True
    while again:
        init_puzzle = []
        six_or_nine = input("Please enter the size of the sudoku puzzle(6 or 9): ") 
        while six_or_nine not in ["6", "9"]:
            six_or_nine = input("It's not that hard. You can do it! Enter 6 or 9: ")
        count = 1
        while count <= int(six_or_nine):
            irow = input("Enter Row " + str(count) + ": ") 
            irow = [int(i) for i in irow.split()]
            init_puzzle.append(irow)
            count += 1
        puzzle = Problem(init_puzzle)
        solution = breadth_first_search(puzzle)
        if solution == None:
            print("No solution could be found.")
        else: print(solution.state)
        startOver = input("If you would like to enter in another sudoku puzzle enter in 'yes'. If you would like to exit the program just hit the <Enter> key: ")
        if startOver != "yes":
            again = False

def make_column_list(state):
    lst = []
    size = len(state)
    for i in range(0, size):
        lst.append([])
        for j in range(0, size):
            lst[i].append(state[j][i])
    return lst

def make_box_list(state):
    lst = []
    size = len(state)
    box_start = 0
    i_mod = 1
    box_start_index = 0
    for i in range(i_mod - 1, size):
        lst.append([])
        box_end = box_start + int(size / 3)
        for j in range(box_start, box_end):
            box_end_index = box_start_index + 3
            for k in range(box_start_index, box_end_index):
                lst[i].append(state[j][k])
        if i_mod % 3 == 0:
            box_start = 0
            box_start_index += 3
        else: box_start += 2
        i_mod += 1
    return lst

def which_box(size, x, y):
    x_start = 0
    x_end = int(size / 3) - 1
    if x >= x_start and x <= x_end:
        if y >= 0 and y <= 2:
            return 0
        if y >= 3 and y <= 5:
            return 3
        if y >= 6 and y <= 8:
            return 6
    x_start += int(size / 3)
    x_end += int(size / 3)
    if x >= x_start and x <= x_end:
        if y >= 0 and y <= 2:
            return 1
        if y >= 3 and y <= 5:
            return 4
        if y >= 6 and y <= 8:
            return 7
    x_start += int(size / 3)
    x_end += int(size / 3)
    if x >= x_start and x <= x_end:
        if y >= 0 and y <= 2:
            return 2
        if y >= 3 and y <= 5:
            return 5
        if y >= 6 and y <= 8:
            return 8
        
        
if __name__ == "__main__":
    sudoku_solver()
