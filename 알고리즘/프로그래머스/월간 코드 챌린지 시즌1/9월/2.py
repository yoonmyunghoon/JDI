def solution(n):
    answer = []
    limit = ((n+1)*n)//2
    data = [[0 for _ in range(i)] for i in range(1, n+1)]
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    flag = 0
    x = 0
    y = 0
    data[0][0] = 1
    for k in range(2, limit+1):
        nx = x + dx[flag]
        ny = y + dy[flag]
        if 0 > nx or nx >= n or ny >= len(data[nx]):
            flag += 1
            flag = flag % 3
        elif data[nx][ny] != 0:
            flag += 1
            flag = flag%3
        nx = x + dx[flag]
        ny = y + dy[flag]
        data[nx][ny] = k
        x = nx
        y = ny
    for i in range(n):
        for j in range(i+1):
            answer.append(data[i][j])
    return answer

print(solution(6))