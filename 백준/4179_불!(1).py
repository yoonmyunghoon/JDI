import sys, collections
sys.stdin = open("4179_불!.txt")

def bfs():
    global Together, result, result1
    if Together[0][2] == 'F':
        visited[Together[0][0]][Together[0][1]] = 1
        visited[Together[-1][0]][Together[-1][1]] = 1
    else:
        visited[Together[-1][0]][Together[-1][1]] = 1
    while Together:
        tx, ty, what = Together.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if G[nx][ny] != '#' and G[nx][ny] != 'F' and visited[nx][ny] == 0:
                    G[nx][ny] = what
                    visited[nx][ny] = visited[tx][ty] + 1
                    Together.append([nx, ny, what])
            else:
                if what == 'J':
                    result1 = visited[tx][ty]
                    return
    result = -1
    return

R, C = map(int, input().split())
G = [list(map(str, input())) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
result = 0
result1 = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
JH = []
FIRE = []
for i in range(R):
    for j in range(C):
        if G[i][j] == 'J':
            JH = [i, j, 'J']
        if G[i][j] == 'F':
            FIRE.append([i, j, 'F'])
Together = collections.deque()
for i in range(len(FIRE)):
    Together.append(FIRE[i])
Together.append(JH)
bfs()
if result == -1:
    print('IMPOSSIBLE')
else:
    print(result1)