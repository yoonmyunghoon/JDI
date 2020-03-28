import sys
sys.stdin = open("2105_디저트 카페.txt")

def isWall(x, y):
    if x < 0 or x >= N: return True
    elif y < 0 or y >= N: return True
    else: return False


def dfs(x, y, type, a, b, n, check):
    # print(type)
    # print(check)
    # print(visited2)
    check[n] += 1
    if check[0] > 0 and check[1] > 0 and check[2] > 0 and check[3] > 0:
        if check[0] == check[2] and check[1] == check[3]:
            if  x == a and y == b:
                type.append(data[x][y])
                types.append(sum(check))
                print(type)
                print(check)
                print(visited2)
                check[n] += 1
                print('chech')
                type.pop()
                check[n] -= 1
                return
    visited1[x][y] = 1
    visited2[data[x][y]] = 1
    type.append(data[x][y])
    if x == a and y == b:
        i = 0
        newX = x + dx[i]
        newY = y + dy[i]
        if visited1[newX][newY] == 0 and visited2[data[newX][newY]] == 0:
            check[n] -= 1
            dfs(newX, newY, type, a, b, i, check)
    else:
        for k in range(2):
            i = (n+k)%4
            newX = x + dx[i]
            newY = y + dy[i]
            if isWall(newX, newY) == False:
                if newX == a and newY == b:
                    dfs(newX, newY, type, a, b, i, check)
                else:
                    if visited1[newX][newY] == 0 and visited2[data[newX][newY]] == 0:
                        dfs(newX, newY, type, a, b, i, check)
    visited1[x][y] = 0
    visited2[data[x][y]] = 0
    type.pop()
    check[n] -= 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited1 = [[0 for _ in range(N)] for _ in range(N)]
    visited2 = [0]*101
    types = []
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]
    for i in range(N-2):
        for j in range(1, N-1):
            type = []
            check = [0, 0, 0, 0]
            dfs(i, j, type, i, j, 0, check)
            # print('ddddd')
    print('#{}'.format(tc), end=' ')
    if types:
        print(max(types))
    else:
        print(-1)
