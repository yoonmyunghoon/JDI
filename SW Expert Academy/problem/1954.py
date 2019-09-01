import sys
sys.stdin = open("input.txt")

def isWall(x, y):
    if x < 0 or x >= N: return True
    elif y < 0 or y >= N: return True
    elif G[x][y] != 0: return True
    else: return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    G = [[0 for _ in range(N)] for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    a = 0
    k = 0
    x = 0
    y = 0
    while 1:
        if a == N*N:
            break
        a += 1
        G[x][y] = a
        newX = x + dx[k % 4]
        newY = y + dy[k % 4]
        if isWall(newX, newY):
            k += 1
            newX = x + dx[k % 4]
            newY = y + dy[k % 4]
        x = newX
        y = newY
    print('#{}'.format(tc))
    for i in G:
        for j in range(N):
            print(i[j], end=' ')
        print()




# n = int(input())
# for y in range(0, n):
#   for x in range(0, n):
#       p = min(x, y, n - x - 1, n - y - 1)
#       if x >= y:
#           q = x + y - 2 * p
#       else:
#           q = (n - 1 - 2 * p) * 4 - (x + y - 2 * p)
#       q += 4 * (p * n - (p * p))
#       print("{:3d}".format(q+1), end="")
#   print()
