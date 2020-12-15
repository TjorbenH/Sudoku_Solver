
class field:
    def __init__(self, y, x, c):
        global curser
        global next
        self.c = c
        self.x = x
        self.y = y
        self.possible = [1,2,3,4,5,6,7,8,9]
        self.origin = [1,2,3,4,5,6,7,8,9]
        self.value = sudoku[y][x]
        self.check(self.possible)
        self.check(self.origin)
        self.variable = True
    #####just for debugging purposes#####
    def __str__(self):
        r = str(self.y)+","+str(self.x)+": "+str(self.origin)+" "+str(self.c)
        return r
    
    #####checkes wich values would be valid according to the soduko rules #####
    def check(self,p):
        global sudoku
        self.to_check = []
        
        #check row
        for i in range(len(sudoku[self.y])):
            test_value = sudoku[self.y][i]
            if test_value in p:
                p.remove(test_value)
               
        #check column
        for i in range(len(sudoku)):
            test_value = sudoku[i][self.x]
            if test_value in p:
                p.remove(test_value)
         
        #check all imidiate neighbours
        if self.x == 0 or self.x == 3 or self.x == 6:
            self.to_check.append([0,1,2])
        elif self.x == 1 or self.x == 4 or self.x == 7:
            self.to_check.append([-1,0,1])
        elif self.x == 2 or self.x == 5 or self.x == 8:
            self.to_check.append([-2,-1,0])
        if self.y == 0 or self.y == 3 or self.y== 6:
            self.to_check.append([0,1,2])
        elif self.y == 1 or self.y == 4 or self.y == 7:
            self.to_check.append([-1,0,1])
        elif self.y == 2 or self.y == 5 or self.y == 8:
            self.to_check.append([-2,-1,0])
        for i in range(3):
            y = self.y + self.to_check[1][i]
            for o in range(3):
                x = self.x + self.to_check [0][o]
                v = sudoku[y][x]
                if v in p:
                    p.remove(v)
     
    #####checks for valid values and does through them one by one#####
    def update(self):
        global curser
        global sudoku
        global changed
        if curser != self.c:
            return
        self.check(self.possible)
        if not self.possible:
            sudoku[self.y][self.x] = 0
            for i in self.origin:
                self.possible.append(i)
            curser -=1
            return
        self.value = self.possible[0]
        self.possible.remove(self.value)
        sudoku[self.y][self.x] = self.value
        curser += 1
        changed = True

#####quick way to print the sudoku state#####
def printL():
    for i in sudoku:
        print(i)
    print()

#####checkes if the curent sudoku is identical with the solution#####
def test():
    global sodoku
    global solved
    global soduko_lösung
    if sudoku == sudoku_lösung:
        printL()
        solved = True
        print("Soduku Solved")
        exit(0)

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
c = 0
for y in range(len(sudoku)):
    for x in range(len(sudoku[1])):
        if sudoku[y][x] == 0:
            fields.append(field(y,x,c))
            c+= 1


next = fields[curser]
printL()
input("start?")

#####loop######
while 1:
    for f in fields:
        f.update()
        if changed == True:
            break
    changed = False
    test()
