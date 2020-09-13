
def solution(maze):
    answer = 0
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    x = 0
    y = 0
    N = len(maze)
    d = 0 # 아래로 보는 방향 / 0 아래 1 왼쪽 2 위쪽 3 오른쪽 / 왼쪽찾으려면 방향에서 (d+3)%4가 인덱스
    while 1:
        if x == N-1 and y == N-1:
            break
        else:
            lx = x + dx[(d+3)%4]
            ly = y + dy[(d+3)%4]
            if lx < 0 or lx > N-1 or ly < 0 or ly > N-1 or maze[lx][ly] == 1:
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or nx > N-1 or ny < 0 or ny > N-1 or maze[nx][ny] == 1:
                    d = (d+1)%4
                else:
                    x = nx
                    y = ny
                    answer += 1
            else:
                d = (d+3)%4
                x = lx
                y = ly
                answer += 1
    return answer

print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]))
