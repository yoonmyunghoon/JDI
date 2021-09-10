from collections import deque


def solution(places):

    def bfs(v, w, input_space):
        visited = [[0 for _ in range(5)] for _ in range(5)]
        visited[v][w] = 1
        queue = deque()
        queue.append([v, w])
        while queue:
            x, y = queue.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx <= 4 and 0 <= ny <= 4:
                    if input_space[nx][ny] != 'X' and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        if input_space[nx][ny] == 'P':
                            if visited[nx][ny] - 1 <= 2:
                                return 0
                        queue.append([nx, ny])
        return 1

    def check_place(input_place):
        for i in range(5):
            for j in range(5):
                if input_place[i][j] == 'P':
                    if bfs(i, j, input_place) == 0:
                        return 0
        return 1

    answer = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for place in places:
        answer.append(check_place(place))
    return answer


places_ex = [
    ["POOOP",
     "OXXOX",
     "OPXPX",
     "OOXOX",
     "POXXP"],
    ["POOPX",
     "OXPXP",
     "PXXXO",
     "OXXXO",
     "OOOPP"],
    ["PXOPX",
     "OXOXP",
     "OXPOX",
     "OXXOP",
     "PXPOX"],
    ["OOOXX",
     "XOOOX",
     "OOOXX",
     "OXOOX",
     "OOOOO"],
    ["PXPXP",
     "XPXPX",
     "PXPXP",
     "XPXPX",
     "PXPXP"]]
print(solution(places_ex))