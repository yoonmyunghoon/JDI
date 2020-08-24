import sys, collections
sys.stdin = open("6593_상범 빌딩.txt")


def bfs(c, a, b):
    visited[c][a][b] = 1
    deq = collections.deque()
    deq.append([c, a, b])
    while deq:
        z, x, y = deq.popleft()
        if x == E_position[1] and y == E_position[2] and z == E_position[0]:
            return visited[z][x][y] - 1
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < R and 0 <= ny < C and 0 <= nz < L:
                if building[nz][nx][ny] != '#' and visited[nz][nx][ny] == 0:
                    deq.append([nz, nx, ny])
                    visited[nz][nx][ny] = visited[z][x][y] + 1
    return -1


while 1:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    dx = [-1, 0, 1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    building = []
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    for i in range(L):
        data = [list(input()) for _ in range(R)]
        building.append(data)
        blank = input()
    S_position = []
    E_position = []
    for z in range(L):
        for x in range(R):
            for y in range(C):
                if building[z][x][y] == 'S':
                    S_position = [z, x, y]
                if building[z][x][y] == 'E':
                    E_position = [z, x, y]
    result = bfs(S_position[0], S_position[1], S_position[2])
    if result == -1:
        print('Trapped!')
    else:
        print('Escaped in {} minute(s).'.format(result))
