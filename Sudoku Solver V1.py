import copy, time

example = [[0, 0, 5, 0, 0, 8, 0, 9, 4],
            [8, 0, 0, 0, 0, 0, 2, 0, 5],
            [0, 0, 0, 9, 5, 3, 0, 0, 0],
            [0, 5, 0, 0, 0, 7, 6, 0, 9],
            [0, 0, 0, 2, 3, 6, 0, 0, 0],
            [2, 0, 6, 5, 0, 0, 0, 4, 0],
            [0, 0, 0, 8, 7, 1, 0, 0, 0],
            [5, 0, 1, 0, 0, 0, 0, 0, 8],
            [6, 8, 0, 4, 0, 0, 1, 0, 0]]

def which_square(position):
    '''return differences to calculate all values in one square'''
    if position[0] in [0,3,6]:
        x = (0,1,2)
    elif position[0] in [1,4,7]:
        x = (-1,0,1)
    elif position[0] in [2,5,8]:
        x = (-2,-1,0)

    if position[1] in [0,3,6]:
        y = (0,1,2)
    elif position[1] in [1,4,7]:
        y = (-1,0,1)
    elif position[1] in [2,5,8]:
        y = (-2,-1,0)
    return (x,y)

def pos_values(position, sudoku):
    '''calculates all the possible values that can be put into that spot'''
    possible = [1,2,3,4,5,6,7,8,9]
    #row
    for filed in sudoku[position[1]]:
        if filed in possible:
            possible.remove(filed)
    #column
    for row in sudoku:
        if row[position[0]] in possible:
            possible.remove(row[position[0]])
    #square
    combis = which_square(position)
    for x_dif in combis[0]:
        for y_dif in combis[1]:
            if x_dif == 0 and y_dif == 0:
                continue
            value = sudoku[position[1] + y_dif][position[0] + x_dif]
            if value in possible:
                possible.remove(value)
    return possible

def get_free(sudoku):
    '''returns all the "free" spots in the sudoku'''
    variables = []
    for y, reihe in enumerate(sudoku):
        for x, wert in enumerate(reihe):
            if wert == 0:
                variables.append((x,y))
    return variables

def sudoku_solver(sudoku):
    '''recursively goes over every possible combination and backtracks to the last changeable spot
    if a dead end is hit'''
    position = get_free(sudoku)[0]
    values = pos_values(position, sudoku)
    if position == (8,8):
        if values:
            sudoku[8][8] = values[0]
            return sudoku
        else:
            return "ERROR"
    else:
        for value in values:
            test = copy.deepcopy(sudoku)
            test[position[1]][position[0]] = value
            possibility = sudoku_solver(test)
            if possibility != "ERROR":
                return possibility
    return "ERROR"


start = time.time()
solution = sudoku_solver(example)
print("solved in: ", time.time() - start)
for row in solution:
    print(row)