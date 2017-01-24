import copy
from queue import Queue

class Puzzle():

    def __init__(self, initial, constraints=None):
        self.initial = initial
        self.constraints = constraints

                  

class Variable():

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def changeValue(self, newValue):
        self.value = newValue


def AC3(variables, domains, constraints):
    queue = Queue()

def MAC():
    return 0

def Forward_Checking():
    return 0

def createDictionary(puzzle):
    variables = {}
    for i in range(0, len(puzzle.initial)):
        for j in range(0, len(puzzle.initial)):
            if i == 0:
                if j == 0:
                    variables["A" + str(j + 1)] = puzzle.initial[i][j]
                if j == 1:
                    variables["A" + str(j + 1)] = puzzle.initial[i][j]
                if j == 2:
                    variables["A" + str(j + 1)] = puzzle.initial[i][j]
                if j == 3:
                    variables["A" + str(j + 1)] = puzzle.initial[i][j]
                if j == 4:
                    variables["A" + str(j + 1)] = puzzle.initial[i][j]
            if i == 1:
                if j == 0:
                    variables["B" + str(j + 1)] = puzzle.initial[i][j]
                if j == 1:
                    variables["B" + str(j + 1)] = puzzle.initial[i][j]
                if j == 2:
                    variables["B" + str(j + 1)] = puzzle.initial[i][j]
                if j == 3:
                    variables["B" + str(j + 1)] = puzzle.initial[i][j]
                if j == 4:
                    variables["B" + str(j + 1)] = puzzle.initial[i][j]
            if i == 2:
                if j == 0:
                    variables["C" + str(j + 1)] = puzzle.initial[i][j]
                if j == 1:
                    variables["C" + str(j + 1)] = puzzle.initial[i][j]
                if j == 2:
                    variables["C" + str(j + 1)] = puzzle.initial[i][j]
                if j == 3:
                    variables["C" + str(j + 1)] = puzzle.initial[i][j]
                if j == 4:
                    variables["C" + str(j + 1)] = puzzle.initial[i][j]
            if i == 3:
                if j == 0:
                    variables["D" + str(j + 1)] = puzzle.initial[i][j]
                if j == 1:
                    variables["D" + str(j + 1)] = puzzle.initial[i][j]
                if j == 2:
                    variables["D" + str(j + 1)] = puzzle.initial[i][j]
                if j == 3:
                    variables["D" + str(j + 1)] = puzzle.initial[i][j]
                if j == 4:
                    variables["D" + str(j + 1)] = puzzle.initial[i][j]
            if i == 4:
                if j == 0:
                    variables["E" + str(j + 1)] = puzzle.initial[i][j]
                if j == 1:
                    variables["E" + str(j + 1)] = puzzle.initial[i][j]
                if j == 2:
                    variables["E" + str(j + 1)] = puzzle.initial[i][j]
                if j == 3:
                    variables["E" + str(j + 1)] = puzzle.initial[i][j]
                if j == 4:
                    variables["E" + str(j + 1)] = puzzle.initial[i][j]
    return variables

def csp_solver():
    again = True
    while again:
        init_puzzle = []
        puzzle_type = ""
        size = int(input("Please enter the size of the puzzle: "))
        while puzzle_type != "CrossMath" and puzzle_type != "Futoshiki":
            puzzle_type = input("Please enter the type of puzzle (CrossMath or Futoshiki): ")
            if puzzle_type == "CrossMath":
                for i in range(0, size):
                    init_puzzle.append([])
                    for j in range(0, size):
                        init_puzzle[i].append(0)
            elif puzzle_type =="Futoshiki":
                count = 1
                while count <= size:
                    irow = input("Enter Row " + str(count) + ": ")
                    irow = [int(i) for i in irow.split()]
                    init_puzzle.append(irow)
                    count += 1
        puzzle = Puzzle(init_puzzle)
        print (puzzle.initial)
        variables = createDictionary(puzzle)
        constraint_list = []
        moreConstraints = True
        while moreConstraints:
            constraint = input("Please input constraints: ")
            constraint_list.append(constraint.split())
            more = input("Are there more constraints? If so enter 'yes'.")
            if more != "yes":
                moreConstraints = False
        startOver = input("If you would like to enter in another sudoku puzzle enter in 'yes'. If you would like to exit the program just hit the <Enter> key: ")
        if startOver != "yes":
            again = False
        
        
if __name__ == "__main__":
    csp_solver()
