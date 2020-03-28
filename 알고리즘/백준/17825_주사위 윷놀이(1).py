import sys
sys.stdin = open("17825_주사위 윷놀이.txt")

# n: 몇번쨰, maxmal: 몇번쨰 말까지 사용할지(0, 1, 2, 3 이 올 수 있음), hap: 합
def dfs(n, maxmal, hap):
    global maximum
    if maxmal > 3:
        return
    if n == len(turns):
        if maximum < hap:
            maximum = hap
        return
    for i in range(4):
        if visited[i] == 0:
            if i == maxmal:
                if maxmal >= 3:
                    continue
                t = mals[i]
                a = types[i]
                mals[i] += turns[n]
                if mals[i] == len(roads[types[i]])-1:
                    if roads_visited[25][-1] == 1 or roads_visited[0][-2] == 1:
                        mals[i] = t
                        break
                if mals[i] > len(roads[types[i]])-1:
                    mals[i] = len(roads[types[i]])
                    if a == 0:
                        roads_visited[a][t - 1] = 0
                    if a == 5:
                        if t >= 9:
                            roads_visited[25][t - 9] = 0
                        else:
                            roads_visited[a][t - 1] = 0
                    if a == 10:
                        if t >= 13:
                            roads_visited[25][t - 13] = 0
                        else:
                            roads_visited[a][t - 1] = 0
                    if a == 15:
                        if t >= 19:
                            roads_visited[25][t - 19] = 0
                        else:
                            roads_visited[a][t - 1] = 0
                    visited[i] = 1
                    dfs(n + 1, maxmal + 1, hap + roads[types[i]][mals[i] - 1])
                    visited[i] = 0
                    if a == 0:
                        roads_visited[a][t - 1] = 1
                    if a == 5:
                        if t >= 9:
                            roads_visited[25][t - 9] = 1
                        else:
                            roads_visited[a][t - 1] = 1
                    if a == 10:
                        if t >= 13:
                            roads_visited[25][t - 13] = 1
                        else:
                            roads_visited[a][t - 1] = 1
                    if a == 15:
                        if t >= 19:
                            roads_visited[25][t - 19] = 1
                        else:
                            roads_visited[a][t - 1] = 1
                    mals[i] = t
                else:
                    if mals[i] <= 4:
                        if roads_visited[20][mals[i]-1] == 0:
                            if 1 <= t <= 4:
                                roads_visited[20][t - 1] = 0
                            roads_visited[20][mals[i]-1] = 1
                            dfs(n + 1, maxmal + 1, hap + roads[types[i]][mals[i] - 1])
                            roads_visited[20][mals[i] - 1] = 0
                            if 1 <= t <= 4:
                                roads_visited[20][t - 1] = 1
                            types[i] = a
                            mals[i] = t
                        else:
                            types[i] = a
                            mals[i] = t

                    if mals[i] == 5:
                        types[i] = 5
                    elif mals[i] == 10:
                        if types[i] == 0:
                            types[i] = 10
                        else:
                            types[i] = 5
                    elif mals[i] == 15:
                        if types[i] == 0:
                            types[i] = 15
                        else:
                            types[i] = 10

                    if types[i] == 5 and mals[i] >= 9:
                        if roads_visited[25][mals[i] - 9] == 0:
                            if t >= 9:
                                roads_visited[25][t - 9] = 0
                            else:
                                roads_visited[a][t - 1] = 0
                            roads_visited[25][mals[i] - 9] = 1
                            dfs(n + 1, maxmal + 1, hap + roads[types[i]][mals[i] - 1])
                            roads_visited[25][mals[i] - 9] = 0
                            if t >= 9:
                                roads_visited[25][t - 9] = 1
                            else:
                                roads_visited[a][t - 1] = 1
                            types[i] = a
                            mals[i] = t
                        else:
                            types[i] = a
                            mals[i] = t
                    elif types[i] == 10 and mals[i] >= 13:
                        if roads_visited[25][mals[i] - 13] == 0:
                            if t >= 13:
                                roads_visited[25][t - 13] = 0
                            else:
                                roads_visited[a][t - 1] = 0
                            roads_visited[25][mals[i] - 13] = 1
                            dfs(n + 1, maxmal + 1, hap + roads[types[i]][mals[i] - 1])
                            roads_visited[25][mals[i] - 13] = 0
                            if t >= 13:
                                roads_visited[25][t - 13] = 1
                            else:
                                roads_visited[a][t - 1] = 1
                            types[i] = a
                            mals[i] = t
                        else:
                            types[i] = a
                            mals[i] = t
                    elif types[i] == 15 and mals[i] >= 19:
                        if roads_visited[25][mals[i] - 19] == 0:
                            if t >= 19:
                                roads_visited[25][t - 19] = 0
                            else:
                                roads_visited[a][t - 1] = 0
                            roads_visited[25][mals[i] - 19] = 1
                            dfs(n + 1, maxmal + 1, hap + roads[types[i]][mals[i] - 1])
                            roads_visited[25][mals[i] - 19] = 0
                            if t >= 19:
                                roads_visited[25][t - 19] = 1
                            else:
                                roads_visited[a][t - 1] = 1
                            types[i] = a
                            mals[i] = t
                        else:
                            types[i] = a
                            mals[i] = t
                    else:
                        if roads_visited[types[i]][mals[i]-1] == 0:
                            if 1 <= t <= 4:
                                roads_visited[20][t - 1] = 0
                            elif t != 0:
                                roads_visited[a][t - 1] = 0
                            roads_visited[types[i]][mals[i]-1] = 1
                            dfs(n+1, maxmal+1, hap+roads[types[i]][mals[i]-1])
                            roads_visited[types[i]][mals[i]-1] = 0
                            if 1 <= t <= 4:
                                roads_visited[20][t - 1] = 1
                            elif t != 0:
                                roads_visited[a][t - 1] = 1
                            types[i] = a
                            mals[i] = t
                        else:
                            types[i] = a
                            mals[i] = t
            else:
                t = mals[i]
                a = types[i]
                mals[i] += turns[n]
                if mals[i] == len(roads[types[i]])-1:
                    if roads_visited[25][-1] == 1 or roads_visited[0][-2] == 1:
                        mals[i] = t
                        break
                if mals[i] > len(roads[types[i]]) - 1:
                    mals[i] = len(roads[types[i]])
                    if a == 0:
                        roads_visited[a][t - 1] = 0
                    if a == 5:
                        if t >= 9:
                            roads_visited[25][t - 9] = 0
                        else:
                            roads_visited[a][t - 1] = 0
                    if a == 10:
                        if t >= 13:
                            roads_visited[25][t - 13] = 0
                        else:
                            roads_visited[a][t - 1] = 0
                    if a == 15:
                        if t >= 19:
                            roads_visited[25][t - 19] = 0
                        else:
                            roads_visited[a][t - 1] = 0
                    visited[i] = 1
                    dfs(n + 1, maxmal, hap + roads[types[i]][mals[i] - 1])
                    visited[i] = 0
                    if a == 0:
                        roads_visited[a][t - 1] = 1
                    if a == 5:
                        if t >= 9:
                            roads_visited[25][t - 9] = 1
                        else:
                            roads_visited[a][t - 1] = 1
                    if a == 10:
                        if t >= 13:
                            roads_visited[25][t - 13] = 1
                        else:
                            roads_visited[a][t - 1] = 1
                    if a == 15:
                        if t >= 19:
                            roads_visited[25][t - 19] = 1
                        else:
                            roads_visited[a][t - 1] = 1
                    mals[i] = t
                else:
                    if mals[i] <= 4:
                        if roads_visited[20][mals[i] - 1] == 0:
                            if 1 <= t <= 4:
                                roads_visited[20][t - 1] = 0
                            roads_visited[20][mals[i] - 1] = 1
                            dfs(n + 1, maxmal, hap + roads[types[i]][mals[i] - 1])
                            roads_visited[20][mals[i] - 1] = 0
                            if 1 <= t <= 4:
                                roads_visited[20][t - 1] = 1
                            types[i] = a
                            mals[i] = t
                        else:
                            types[i] = a
                            mals[i] = t

                    if mals[i] == 5:
                        types[i] = 5
                    elif mals[i] == 10:
                        if types[i] == 0:
                            types[i] = 10
                        else:
                            types[i] = 5
                    elif mals[i] == 15:
                        if types[i] == 0:
                            types[i] = 15
                        else:
                            types[i] = 10

                    if types[i] == 5 and mals[i] >= 9:
                        if roads_visited[25][mals[i] - 9] == 0:
                            if t >= 9:
                                roads_visited[25][t - 9] = 0
                            else:
                                roads_visited[a][t - 1] = 0
                            roads_visited[25][mals[i] - 9] = 1
                            dfs(n + 1, maxmal, hap + roads[types[i]][mals[i] - 1])
                            roads_visited[25][mals[i] - 9] = 0
                            if t >= 9:
                                roads_visited[25][t - 9] = 1
                            else:
                                roads_visited[a][t - 1] = 1
                            types[i] = a
                            mals[i] = t
                        else:
                            types[i] = a
                            mals[i] = t
                    elif types[i] == 10 and mals[i] >= 13:
                        if roads_visited[25][mals[i] - 13] == 0:
                            if t >= 13:
                                roads_visited[25][t - 13] = 0
                            else:
                                roads_visited[a][t - 1] = 0
                            roads_visited[25][mals[i] - 13] = 1
                            dfs(n + 1, maxmal, hap + roads[types[i]][mals[i] - 1])
                            roads_visited[25][mals[i] - 13] = 0
                            if t >= 13:
                                roads_visited[25][t - 13] = 1
                            else:
                                roads_visited[a][t - 1] = 1
                            types[i] = a
                            mals[i] = t
                        else:
                            types[i] = a
                            mals[i] = t
                    elif types[i] == 15 and mals[i] >= 19:
                        if roads_visited[25][mals[i] - 19] == 0:
                            if t >= 19:
                                roads_visited[25][t - 19] = 0
                            else:
                                roads_visited[a][t - 1] = 0
                            roads_visited[25][mals[i] - 19] = 1
                            dfs(n + 1, maxmal, hap + roads[types[i]][mals[i] - 1])
                            roads_visited[25][mals[i] - 19] = 0
                            if t >= 19:
                                roads_visited[25][t - 19] = 1
                            else:
                                roads_visited[a][t - 1] = 1
                            types[i] = a
                            mals[i] = t
                        else:
                            types[i] = a
                            mals[i] = t
                    else:
                        if roads_visited[types[i]][mals[i] - 1] == 0:
                            if 1 <= t <= 4:
                                roads_visited[20][t - 1] = 0
                            elif t != 0:
                                roads_visited[a][t - 1] = 0
                            roads_visited[types[i]][mals[i] - 1] = 1
                            dfs(n + 1, maxmal, hap + roads[types[i]][mals[i] - 1])
                            roads_visited[types[i]][mals[i] - 1] = 0
                            if 1 <= t <= 4:
                                roads_visited[20][t - 1] = 1
                            elif t != 0:
                                roads_visited[a][t - 1] = 1
                            types[i] = a
                            mals[i] = t
                        else:
                            types[i] = a
                            mals[i] = t
roads = {
    0: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0],
    5: [2, 4, 6, 8, 10, 13, 16, 19, 25, 30, 35, 40, 0],
    10: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30, 35, 40, 0],
    15: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 27, 26, 25, 30, 35, 40, 0]
}
roads_visited = {
    0: [0]*21,
    5: [0]*13,
    10: [0]*17,
    15: [0]*23,
    20: [0]*4,
    25: [0]*4
}
turns = list(map(int, input().split()))
mals = [0, 0, 0, 0]
types = [0, 0, 0, 0]
visited = [0, 0, 0, 0]
maximum = 0
dfs(0, 0, 0)
print(maximum)

