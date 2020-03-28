import sys
import time
sys.stdin = open("input.txt")
start_time = time.time()

def isWall(y, x):
    if 0 >= x or x >= 14: return True
    elif 0 >= y or y >= 14: return True
    elif G[y][x] == 1: return True
    else: return False

def dfs(y, x):
    global result
    global count
    global end
    count += 1
    if count >= 13 * 13:
        end = 1
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if G[newY][newX] == 3:
            result = 1
            end = 1
            break
        if isWall(newY, newX) == False:
            if visited[newY][newX] == 0:
                x2 = newX
                y2 = newY
                visited[y2][x2] = 2
                dfs(y2, x2)

T = 10
for tc in range(1, T+1):
    N = int(input())
    G = [list(map(int, input())) for _ in range(16)]
    visited = [[0 for _ in range(16)] for _ in range(16)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    x = 1
    y = 1
    result = 0
    count = 0
    end = 0
    G[x][y] = 1
    while 1:
        dfs(y, x)
        if end == 1:
            break

    print('#{} {}'.format(tc, result))
print(time.time() - start_time , 'seconds')


