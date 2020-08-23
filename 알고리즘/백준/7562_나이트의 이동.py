import sys, collections
sys.stdin = open("7562_나이트의 이동.txt")


def bfs(a, b):
    visited[a][b] = 1
    deq = collections.deque()
    deq.append([a, b])
    while deq:
        x, y = deq.popleft()
        if x == des_x and y == des_y:
            return visited[des_x][des_y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I:
                if visited[nx][ny] == 0:
                    deq.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1


T = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
for tc in range(T):
    I = int(input())
    visited = [[0 for _ in range(I)] for _ in range(I)]
    now_x, now_y = map(int, input().split())
    des_x, des_y = map(int, input().split())
    print(bfs(now_x, now_y)-1)