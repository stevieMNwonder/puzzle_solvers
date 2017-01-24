from copy import deepcopy
from queue import Queue
import time

class Problem(object):

    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def actions(self, state): #goes through actions of the current node being observed to generate its children
        action_list = []
        for i in range(0, 3):
            for j in range(0, 3):
                if (state[i].peek() > 0 and state[j].peek() == 0):
                    action_list.append([i, j])
                elif (state[i].peek() < state[j].peek()) and state[i].peek() > 0:
                    action_list.append([i, j])
        return action_list

    def result(self, state, action):  #returns the state of the node after a given action is implemented on the current state of the node
        state_copy = deepcopy(state)
        state_copy[action[1]].push(state_copy[action[0]].pop())
        return state_copy

    def BBFS_goal_test(self, initial, goal):  #used to check and see if the initial node state is the same as the goal node state for the bidirectional search
        if initial[0].stack == goal[0].stack and initial[1].stack == goal[1].stack and initial[2].stack == goal[2].stack:
            return True
        return False

    def BFS_goal_test(self, state):  #used in the breadth-first-search to determine whether the current node state is the same as the goal node state
        if state[0].stack == self.goal[0].stack and state[1].stack == self.goal[1].stack and state[2].stack == self.goal[2].stack:
            return True
        return False

class Node(object):  #node in a search tree. Contains the current state of the tree and connects the tree through keeping track of its children/parent

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def expand(self, problem):   # List the nodes reachable in one step from this node.
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action): #returns the child node of the current node after a given action
        next = problem.result(self.state, action)
        return Node(next, self)

    def compare_node(self, node): #used to compare the current node to another node to see if they are equal
        if (self.state[0].same_stack(node.state[0])) and (self.state[1].same_stack(node.state[1])) and (self.state[2].same_stack(node.state[2])):
            return True
        return False

    def compare_state(self, state): #used to compare the state of the current node to the state of another node to see if they are equal
        if (self.state[0].same_stack(state[0])) and (self.state[1].same_stack(state[1])) and (self.state[2].same_stack(state[2])):
            return True
        return False

    def compare_node_list(self, list):  #used to compare the current node to a list of other nodes(the frontier)
        for x in list:
            if self.compare_node(x):
                return True
        return False

    def compare_state_list(self, list):   #used to compare the state of the current node to a list of states of other nodes(the explored list)
        for x in list:
            if self.compare_state(x):
                return True
        return False
        


class Stack: #Created a stack data structure to more easily manipulate moves

    def __init__(self, stack):
        self.stack = stack

    def pop(self):     #returns first item of list and removes it
        if self.stack:
            return self.stack.pop(0)

    def push(self, x):      #inserts element into the front of list
        self.stack.insert(0, x)

    def peek(self):   #returns the first item of the list but does not remove it like pop
        if self.stack:
            return self.stack[0]
        return 0

    def same_stack(self, stack):     #checks if two stacks are the same
        if self.stack == stack.stack:
            return True
        return False



def bidirectional_breadth_first_search(problem):  #essentially the same as breadth first search except we need to make two of everything. One for the initial start and one for the goal start.
    start_time = time.time()      #used to measure total time that this function takes
    start_node = Node(problem.initial)   #initial node from the starting state
    goal_node = Node(problem.goal)    #initial node starting from the goal state
    if problem.BBFS_goal_test(start_node.state, goal_node.state):
        print("--- %s seconds ---" % (time.time() - start_time))
        return start_node
    start_frontier = []
    goal_frontier = []
    start_frontier.append(start_node)
    goal_frontier.append(goal_node)
    start_explored = []
    goal_explored = []
    while start_frontier or goal_frontier:
        start_node = start_frontier.pop()
        goal_node = goal_frontier.pop()
        start_explored.append(start_node.state)
        goal_explored.append(goal_node.state)
        for child in start_node.expand(problem): #goes through all children of current forward searching node and adds them to the forward frontier if they are not already explored or in the frontier 
            if not(child.compare_state_list(start_explored)) and not(child.compare_node_list(start_frontier)):
                if child.compare_node_list(goal_frontier):   #checks to see if the current forward child node is in the backward frontier which means a solution was found
                    print(len(start_explored))
                    print(len(goal_explored))
                    print("--- %s seconds ---" % (time.time() - start_time))
                    return child
                start_frontier.append(child)
        for child in goal_node.expand(problem): #goes through all children of current backward searching node and adds them to the backward frontier if they are not already explored or in the frontier
            if not(child.compare_state_list(goal_explored)) and not(child.compare_node_list(goal_frontier)):
                if child.compare_node_list(start_frontier):    #checks to see if the current backward child node is in the forward frontier which means a solution was found
                    print(len(start_explored))
                    print(len(goal_explored))
                    print("--- %s seconds ---" % (time.time() - start_time))
                    return child
                goal_frontier.append(child)
    return None


def breadth_first_search(problem):
    start_time = time.time()   #used to measure total time that this function takes
    node = Node(problem.initial)
    if problem.BFS_goal_test(node.state): #checks to see if the initial node happens to be the goal node
        print("--- %s seconds ---" % (time.time() - start_time))
        return node
    frontier = []  #list to store children nodes. determines the order in which the tree is traversed
    frontier.append(node)
    explored = []    #list to keep track of states that have already been explored
    while frontier:
        node = frontier.pop()
        explored.append(node.state)
        for child in node.expand(problem):  #goes through all children of current node and adds them to the frontier if they are not already explored or in the frontier
            if not(child.compare_state_list(explored)) and not(child.compare_node_list(frontier)):
                if problem.BFS_goal_test(child.state): #checks if the current child node is the same as the goal node
                    print(len(explored))
                    print("--- %s seconds ---" % (time.time() - start_time))
                    return child
                frontier.append(child) 
    return None

#test cases
one_ring = Problem([Stack([1]), Stack([]), Stack([])], [Stack([]), Stack([]), Stack([1])])
two_rings = Problem([Stack([1, 2]), Stack([]), Stack([])], [Stack([]), Stack([]), Stack([1, 2])])
three_rings = Problem([Stack([1, 2, 3]), Stack([]), Stack([])], [Stack([]), Stack([]), Stack([1, 2, 3])])
four_rings = Problem([Stack([1, 2, 3, 4]), Stack([]), Stack([])], [Stack([]), Stack([]), Stack([1, 2, 3, 4])])
five_rings = Problem([Stack([1, 2, 3, 4, 5]), Stack([]), Stack([])], [Stack([]), Stack([]), Stack([1, 2, 3, 4, 5])])
six_rings = Problem([Stack([1, 2, 3, 4, 5, 6]), Stack([]), Stack([])], [Stack([]), Stack([]), Stack([1, 2, 3, 4, 5, 6])])
seven_rings = Problem([Stack([1, 2, 3, 4, 5, 6, 7]), Stack([]), Stack([])], [Stack([]), Stack([]), Stack([1, 2, 3, 4, 5, 6, 7])])
eight_rings = Problem([Stack([1, 2, 3, 4, 5, 6, 7, 8]), Stack([]), Stack([])], [Stack([]), Stack([]), Stack([1, 2, 3, 4, 5, 6, 7, 8])])
nine_rings = Problem([Stack([1, 2, 3, 4, 5, 6, 7, 8, 9]), Stack([]), Stack([])], [Stack([]), Stack([]), Stack([1, 2, 3, 4, 5, 6, 7, 8, 9])])
ten_rings = Problem([Stack([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Stack([]), Stack([])], [Stack([]), Stack([]), Stack([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])])

print("BFS 1"),
breadth_first_search(one_ring)
print("BBFS 1"),
bidirectional_breadth_first_search(one_ring)
print("BFS 2"),
breadth_first_search(two_rings)
print("BBFS 2"),
bidirectional_breadth_first_search(two_rings)
print("BFS 3"),
breadth_first_search(three_rings)
print("BBFS 3"),
bidirectional_breadth_first_search(three_rings)
print("BFS 4"),
breadth_first_search(four_rings)
print("BBFS 4"),
bidirectional_breadth_first_search(four_rings)
print("BFS 5"),
breadth_first_search(five_rings)
print("BBFS 5"),
bidirectional_breadth_first_search(five_rings)
print("BFS 6"),
breadth_first_search(six_rings)
print("BBFS 6"),
bidirectional_breadth_first_search(six_rings)
print("BFS 7"),
breadth_first_search(seven_rings)
print("BBFS 7"),
bidirectional_breadth_first_search(seven_rings)
print("BFS 8"),
breadth_first_search(eight_rings)
print("BBFS 8"),
bidirectional_breadth_first_search(eight_rings)
print("BFS 9"),
breadth_first_search(nine_rings)
print("BBFS 9"),
bidirectional_breadth_first_search(nine_rings)
#print("BFS 10"),
#breadth_first_search(ten_rings)
#print("BBFS 10"),
#bidirectional_breadth_first_search(ten_rings)
