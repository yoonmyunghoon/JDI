import sys
sys.stdin = open("4574_스도미노쿠.txt")


def row_check(num, x):
    if num in Board[x]:
        return 0
    return 1


def col_check(num, y):
    for i in range(9):
        if Board[i][y] == num:
            return 0
    return 1


def box_check(num, x, y):
    mx = (x // 3)*3
    my = (y // 3)*3
    if num in Board[mx][my:my+3]+Board[mx+1][my:my+3]+Board[mx+2][my:my+3]:
        return 0
    return 1


def find_sudoku(n):
    global tmp
    if tmp == 1:
        return
    if n == len_positions:
        tmp = 1
        for d in Board:
            print(''.join(map(str, d)))
        return
    x = positions[n][0]
    y = positions[n][1]
    if Board[x][y] != 0:
        find_sudoku(n+1)
    else:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<9 and 0<=ny<9 and Board[nx][ny] == 0:
                for num1 in range(1, 10):
                    if row_check(num1, x) and col_check(num1, y) and box_check(num1, x, y):
                        for num2 in range(1, 10):
                            if num1 != num2 and row_check(num2, nx) and col_check(num2, ny) and box_check(num2, nx, ny):
                                n1, n2 = domino_arrange(num1, num2)
                                if domino_check[n1][n2] == 0:
                                    Board[x][y] = num1
                                    Board[nx][ny] = num2
                                    domino_check[n1][n2] = 1
                                    find_sudoku(n+1)
                                    Board[x][y] = 0
                                    Board[nx][ny] = 0
                                    domino_check[n1][n2] = 0


def domino_arrange(n1, n2):
    if n1 > n2:
        return n2, n1
    else:
        return n1, n2


tc = 0
dx = [0, 1]
dy = [1, 0]
while 1:
    tc += 1
    N = int(input())

    # 테스트케이스가 더 있는지 체크
    if N == 0:
        break

    # 입력
    Board = [[0 for _ in range(9)] for _ in range(9)]
    domino_check = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(N):
        a, a_p, b, b_p = map(str, input().split())
        a_x = ord(a_p[0]) - 64
        a_y = int(a_p[1])
        b_x = ord(b_p[0]) - 64
        b_y = int(b_p[1])
        Board[a_x - 1][a_y - 1] = int(a)
        Board[b_x - 1][b_y - 1] = int(b)
        small, big = domino_arrange(int(a), int(b))
        domino_check[small][big] = 1
    numbers = list(input().split())
    for i in range(9):
        x = ord(numbers[i][0]) - 64
        y = int(numbers[i][1])
        Board[x - 1][y - 1] = i + 1

    # 비어있는 위치를 체크하기 위한 리스트
    positions = []
    for i in range(9):
        for j in range(9):
            if Board[i][j] == 0:
                positions.append((i, j))
    len_positions = len(positions)

    # 출력
    tmp = 0
    print("Puzzle", tc)
    find_sudoku(0)

