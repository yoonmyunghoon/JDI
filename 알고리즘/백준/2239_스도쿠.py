import sys
sys.stdin = open("2239_스도쿠.txt")


def row_check(num, x):
    if num in data[x]:
        return 0
    return 1


def col_check(num, y):
    for i in range(9):
        if data[i][y] == num:
            return 0
    return 1


def box_check(num, x, y):
    mx = (x // 3)*3
    my = (y // 3)*3
    if num in data[mx][my:my+3]+data[mx+1][my:my+3]+data[mx+2][my:my+3]:
        return 0
    return 1


def find_sudoku(n):
    if n == len_positions:
        for d in data:
            print(''.join(map(str, d)))
        sys.exit()
    x = positions[n][0]
    y = positions[n][1]
    for num in range(1, 10):
        if row_check(num, x) and col_check(num, y) and box_check(num, x, y):
            data[x][y] = num
            find_sudoku(n+1)
            data[x][y] = 0


data = [list(map(int, input())) for _ in range(9)]
# visited = [[0 for _ in range(9)] for _ in range(9)]
# for i in range(9):
#     for j in range(9):
#         if data[i][j] != 0:
#             visited[i][j] = 1

positions = []
for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            positions.append((i, j))
len_positions = len(positions)
find_sudoku(0)

