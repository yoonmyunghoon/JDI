import sys
sys.stdin = open("4574_스도미노쿠.txt")

tc = 0
while 1:
    tc += 1
    N = int(input())
    if N == 0:
        break
    Board = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(N):
        a, a_p, b, b_p = map(str, input().split())
        a_x = ord(a_p[0]) - 64
        a_y = int(a_p[1])
        b_x = ord(b_p[0]) - 64
        b_y = int(b_p[1])
        Board[a_x - 1][a_y - 1] = int(a)
        Board[b_x - 1][b_y - 1] = int(b)
    data = list(input().split())
    for i in range(9):
        x = ord(data[i][0]) - 64
        y = int(data[i][1])
        Board[x - 1][y - 1] = i + 1
    print("Puzzle ", tc)
    for i in Board:
        print(i)
    print()

