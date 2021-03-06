import time


#####class wich is going to represent fiels on the sudoku grid#####
class field:
    #####assigning all important values#####
    def __init__(self, y, x, ID):
        global curser
        global next
        self.ID = ID  # used to keep track of all changable fields
        self.x = x  # x coordinate in grid
        self.y = y  # y coordinate in grid
        self.possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # wich values can be put into the spot
        self.origin = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # wich values can be put in the spot at the start of the game
        self.value = sudoku[y][x]  # stores the curent value of the field
        self.check(self.possible)
        self.check(self.origin)

    #####checkes wich values would be valid according to the soduko rules #####
    def check(self, storage):
        global sudoku
        self.to_check = []

        # check row
        for i in range(len(sudoku[self.y])):
            test_value = sudoku[self.y][i]
            if test_value in storage:
                storage.remove(test_value)

        # check column
        for i in range(len(sudoku)):
            test_value = sudoku[i][self.x]
            if test_value in storage:
                storage.remove(test_value)

        # check all imidiate neighbours
        if self.x == 0 or self.x == 3 or self.x == 6:
            self.to_check.append([0, 1, 2])
        elif self.x == 1 or self.x == 4 or self.x == 7:
            self.to_check.append([-1, 0, 1])
        elif self.x == 2 or self.x == 5 or self.x == 8:
            self.to_check.append([-2, -1, 0])
        if self.y == 0 or self.y == 3 or self.y == 6:
            self.to_check.append([0, 1, 2])
        elif self.y == 1 or self.y == 4 or self.y == 7:
            self.to_check.append([-1, 0, 1])
        elif self.y == 2 or self.y == 5 or self.y == 8:
            self.to_check.append([-2, -1, 0])
        for i in range(3):
            y = self.y + self.to_check[1][i]
            for o in range(3):
                x = self.x + self.to_check[0][o]
                s = sudoku[y][x]
                if s in storage:
                    storage.remove(s)

    #####checks for valid values and does through them one by one#####
    def update(self):
        global curser  # keeps track of what field should be edited right now
        global sudoku
        global changed
        if curser != self.ID:
            return
        self.check(self.possible)  # refreshing possible values
        if not self.possible:  # if every possible value has been tried
            sudoku[self.y][self.x] = 0  # the curser goes to the previous changable field
            for i in self.origin:
                self.possible.append(i)
            curser -= 1
            return
        self.value = self.possible[0]  # test the next possible value
        self.possible.remove(self.value)
        sudoku[self.y][self.x] = self.value
        curser += 1
        changed = True


#####quick way to print the sudoku state#####
def print_sudoku():
    for i in sudoku:
        print(i)
    print()


#####checkes if the curent sudoku is identical with the solution#####
def test():
    global sodoku
    global solved
    global soduko_lösung
    if sudoku == sudoku_lösung:
        print_sudoku()
        solved = True
        print("Soduku Solved")
    return True


#####This is a Test Sudoku so you can plug and play this programm ######

sudoku = [
    [0, 1, 2, 0, 0, 0, 5, 7, 0],
    [6, 0, 0, 5, 0, 1, 0, 0, 4],
    [4, 0, 0, 0, 2, 0, 0, 0, 8],
    [0, 2, 0, 0, 1, 0, 0, 5, 0],
    [0, 0, 4, 9, 0, 7, 8, 0, 0],
    [0, 7, 0, 0, 8, 0, 0, 1, 0],
    [7, 0, 0, 0, 9, 0, 0, 0, 5],
    [5, 0, 0, 4, 0, 8, 0, 0, 6],
    [0, 3, 8, 0, 0, 0, 9, 4, 0]
]
sudoku_lösung = [
    [9, 1, 2, 8, 4, 6, 5, 7, 3],
    [6, 8, 3, 5, 7, 1, 2, 9, 4],
    [4, 5, 7, 3, 2, 9, 1, 6, 8],
    [8, 2, 9, 6, 1, 3, 4, 5, 7],
    [1, 6, 4, 9, 5, 7, 8, 3, 2],
    [3, 7, 5, 2, 8, 4, 6, 1, 9],
    [7, 4, 6, 1, 9, 2, 3, 8, 5],
    [5, 9, 1, 4, 3, 8, 7, 2, 6],
    [2, 3, 8, 7, 6, 5, 9, 4, 1]
]

#####main######
#####inits#####
solved = False
curser = 0
changed = False
fields = []
ID = 0
# creating a field object for all changable
for y in range(len(sudoku)):
    for x in range(len(sudoku[1])):
        if sudoku[y][x] == 0:
            fields.append(field(y, x, ID))
            ID += 1

##printing the initialistion message
next = fields[curser]
print_sudoku()
input("start?")

#####loop######
start = time.time()
while 1:
    for f in fields:
        f.update()  # updating every single field object
        if changed == True:
            break
    changed = False
    if test(): # checking if the sudoku is solved
        break
print("solved in: ", time.time() - start)