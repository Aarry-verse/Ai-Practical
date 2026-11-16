# Practical 6: Sudoku Solver Using Backtracking

def solve(b):
    for i in range(9):
        for j in range(9):
            if b[i][j] == 0:
                for n in range(1, 10):
                    if (n not in b[i] and
                        all(b[x][j] != n for x in range(9)) and
                        all(b[x][y] != n
                        for x in range(i//3*3, i//3*3+3)
                        for y in range(j//3*3, j//3*3+3))):

                        b[i][j] = n
                        if solve(b):
                            return True
                        b[i][j] = 0
                return False
    return True

b = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]

solve(b)

for row in b:
    print(row)
