from queue import Queue
import time

class Maze():

    def __init__(self, maze, starting_point, size=None):
        self.maze = maze
        self.starting_point = starting_point
        self.size = len(maze)

    def get_x(self, coordinates):
        return coordinates[0]

    def get_y(self, coordinates):
        return coordinates[1]
    


class Node():

    def __init__(self, index):
        self.index = index
        

#does not keep track of explored set
def tree_search(maze):
    start_time = time.time()
    node = Node(maze.starting_point)
    frontier = Queue()
    frontier.put(node)
    while not(frontier.empty()):
        node = frontier.get()
        if maze.maze[maze.get_x(node.index)][maze.get_y(node.index)] == 1: #checks if current node is at the goal
            print("--- %s seconds ---" % (time.time() - start_time))
            return node.index
        if maze.get_x(node.index) == 0 and maze.get_y(node.index) == 0: #checks if current node is upper left corner
            new_node = Node([1, 0])
            frontier.put(new_node)
            new_node = Node([0, 1])
            frontier.put(new_node)
        elif maze.get_x(node.index) == (maze.size - 1) and maze.get_y(node.index) == (maze.size - 1):  #checks if current node is lower right corner
            new_node = Node([(maze.size - 2), (maze.size - 1)])
            frontier.put(new_node)
            new_node = Node([(maze.size - 1), (maze.size - 2)])
            frontier.put(new_node)
        elif maze.get_x(node.index) == 0 and maze.get_y(node.index) == (maze.size - 1):   #checks if current node is upper right corner
            new_node = Node([1, (maze.size - 1)])
            frontier.put(new_node)
            new_node = Node([0, (maze.size - 2)])
            frontier.put(new_node)
        elif maze.get_x(node.index) == (maze.size - 1) and maze.get_y(node.index) == 0:   #checks if current node is lower left corner
            new_node = Node([(maze.size - 1), 1])
            frontier.put(new_node)
            new_node = Node([(maze.size - 2), 0])
            frontier.put(new_node)
        elif maze.get_x(node.index) == 0 and (maze.get_y(node.index) > 0 and maze.get_y(node.index) < (maze.size - 1)):   #checks if current node is on top side
            new_node = Node([0, (maze.get_y(node.index) - 1)])
            frontier.put(new_node)
            new_node = Node([0, (maze.get_y(node.index) + 1)])
            frontier.put(new_node)
            new_node = Node([1, (maze.get_y(node.index))])
            frontier.put(new_node)
        elif (maze.get_x(node.index) > 0 and maze.get_x(node.index) < (maze.size - 1)) and maze.get_y(node.index) == 0:   #checks if current node is on left side
            new_node = Node([(maze.get_x(node.index) - 1), 0])
            frontier.put(new_node)
            new_node = Node([(maze.get_x(node.index) + 1), 0])
            frontier.put(new_node)
            new_node = Node([(maze.get_x(node.index)), 1])
            frontier.put(new_node)
        elif maze.get_x(node.index) == (maze.size - 1) and (maze.get_y(node.index) > 0 and maze.get_y(node.index) < (maze.size - 1)):   #checks if current node is on bottom side
            new_node = Node([(maze.size - 1), (maze.get_y(node.index) - 1)])
            frontier.put(new_node)
            new_node = Node([(maze.size - 1), (maze.get_y(node.index) + 1)])
            frontier.put(new_node)
            new_node = Node([(maze.size - 2), (maze.get_y(node.index))])
            frontier.put(new_node)
        elif (maze.get_x(node.index) > 0 and maze.get_x(node.index) < (maze.size - 1)) and maze.get_y(node.index) == (maze.size - 1):   #checks if current node is on right side
            new_node = Node([(maze.get_x(node.index) - 1), (maze.size - 1)])
            frontier.put(new_node)
            new_node = Node([(maze.get_x(node.index) + 1), (maze.size - 1)])
            frontier.put(new_node)
            new_node = Node([(maze.get_x(node.index)), (maze.size - 2)])
            frontier.put(new_node)
        else:   #checks if current node is not touching any sides or corners
            new_node = Node([(maze.get_x(node.index) - 1), (maze.get_y(node.index))])
            frontier.put(new_node)
            new_node = Node([(maze.get_x(node.index)), (maze.get_y(node.index) - 1)])
            frontier.put(new_node)
            new_node = Node([(maze.get_x(node.index) + 1), (maze.get_y(node.index))])
            frontier.put(new_node)
            new_node = Node([(maze.get_x(node.index)), (maze.get_y(node.index) + 1)])
            frontier.put(new_node)
    print("--- %s seconds ---" % (time.time() - start_time))
    return False


#keeps track of explored set
def graph_search(maze):
    start_time = time.time()
    node = Node(maze.starting_point)
    frontier = Queue()
    frontier.put(node)
    explored = []
    while not(frontier.empty()):
        node = frontier.get()
        if maze.maze[maze.get_x(node.index)][maze.get_y(node.index)] == 1:   #checks if current node is at the goal
            print("--- %s seconds ---" % (time.time() - start_time))
            return node.index
        explored.append(node)
        if maze.get_x(node.index) == 0 and maze.get_y(node.index) == 0:   #checks if current node is upper left corner
            new_node = Node([1, 0])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([0, 1])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
        elif maze.get_x(node.index) == (maze.size - 1) and maze.get_y(node.index) == (maze.size - 1):   #checks if current node is lower right corner
            new_node = Node([(maze.size - 2), (maze.size - 1)])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([(maze.size - 1), (maze.size - 2)])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
        elif maze.get_x(node.index) == 0 and maze.get_y(node.index) == (maze.size - 1):   #checks if current node is upper right corner
            new_node = Node([1, (maze.size - 1)])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([0, (maze.size - 2)])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
        elif maze.get_x(node.index) == (maze.size - 1) and maze.get_y(node.index) == 0:   #checks if current node is lower left corner
            new_node = Node([(maze.size - 1), 1])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([(maze.size - 2), 0])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
        elif maze.get_x(node.index) == 0 and (maze.get_y(node.index) > 0 and maze.get_y(node.index) < (maze.size - 1)):   #checks if current node is on top side
            new_node = Node([0, (maze.get_y(node.index) - 1)])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([0, (maze.get_y(node.index) + 1)])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([1, (maze.get_y(node.index))])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
        elif (maze.get_x(node.index) > 0 and maze.get_x(node.index) < (maze.size - 1)) and maze.get_y(node.index) == 0:   #checks if current node is on left side
            new_node = Node([(maze.get_x(node.index) - 1), 0])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([(maze.get_x(node.index) + 1), 0])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([(maze.get_x(node.index)), 1])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
        elif maze.get_x(node.index) == (maze.size - 1) and (maze.get_y(node.index) > 0 and maze.get_y(node.index) < (maze.size - 1)):   #checks if current node is on bottom side
            new_node = Node([(maze.size - 1), (maze.get_y(node.index) - 1)])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([(maze.size - 1), (maze.get_y(node.index) + 1)])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([(maze.size - 2), (maze.get_y(node.index))])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
        elif (maze.get_x(node.index) > 0 and maze.get_x(node.index) < (maze.size - 1)) and maze.get_y(node.index) == (maze.size - 1):   #checks if current node is on right side
            new_node = Node([(maze.get_x(node.index) - 1), (maze.size - 1)])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([(maze.get_x(node.index) + 1), (maze.size - 1)])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([(maze.get_x(node.index)), (maze.size - 2)])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
        else:   #checks if current node is not touching any sides or corners
            new_node = Node([(maze.get_x(node.index) - 1), (maze.get_y(node.index))])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([(maze.get_x(node.index)), (maze.get_y(node.index) - 1)])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([(maze.get_x(node.index) + 1), (maze.get_y(node.index))])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
            new_node = Node([(maze.get_x(node.index)), (maze.get_y(node.index) + 1)])
            for noder in explored:
                if new_node.index == noder.index:
                    break
            else: frontier.put(new_node)
    print("--- %s seconds ---" % (time.time() - start_time))
    return False
       
        
maze_one = Maze([[1]], [0,0])

maze_two = Maze([[0, 0],
                 [0, 1]], [0, 0])

maze_three = Maze([[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 1]], [0, 0])

maze_four = Maze([[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]], [0,0])

maze_five = Maze([[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1]], [0, 0])

maze_ten = Maze([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]], [0,0]) 
                 

maze_twenty = Maze([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]], [0,0])
