import sys
sys.stdin = open("14499_주사위 굴리기.txt")


def moving(x, y, d):
    if MAP[x][y] == 0:
        MAP[x][y] = cube[cube_position[1 + dx[d]][1 + dy[d]]]
    else:
        cube[cube_position[1 + dx[d]][1 + dy[d]]] = MAP[x][y]
        MAP[x][y] = 0
    tmp = cube_position[1][1]
    cube_position[1 + dx[d]][1 + dy[d]] = cube_position[1][1]
    cube_position[1][1] = cube_position[1 - dx[d]][1 - dy[d]]
    cube_position[1 - dx[d]][1 - dy[d]] = 7 - tmp
    print(cube[cube_position[1][1]])


N, M, x, y, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
operations = list(map(int, input().split()))
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
cube_position = [[0, 2, 0],
                 [4, 1, 3],
                 [0, 5, 0]]
cube = [-1, 0, 0, 0, 0, 0, 0]

for d in operations:
    if 0 <= x + dx[d] < N and 0 <= y + dy[d] < M:
        x = x + dx[d]
        y = y + dy[d]
        moving(x, y, d)
    else:
        continue
