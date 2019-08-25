import sys
sys.stdin = open("input.txt")


def dfs(v):
    for w in range(1, V+1):
        if graph[v][w] == 1:
            check[w] -= 1


T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    check = [0 for _ in range(V+1)]
    result = []
    for i in range(E):
        graph[data[i*2]][data[i*2+1]] = 1
    for i in range(1, len(data), 2):
        check[data[i]] += 1
    # for i in range(len(graph)):
    while 1:
        for i in range(1, V+1):
            if check[i] == 0 and visited[i] == 0:
                visited[i] = 1
                result.append(i)
                dfs(i)
        if visited.count(1) == V:
            break

    print('#{}'.format(tc), end=' ')
    for i in result:
        print(i, end=' ')
    print()

# def dfs(x):
#    for q in range(1, V+1):
#        if nxn[x][q] == 1:
#            ccc[q] -= 1
# T = 10
# for test in range(T):
#    V, E = map(int, input().split())
#    nxn = [[0 for _ in range(V+1)] for _ in range(V + 1)]
#    visited = [0 for _ in range(V + 2)]
#    arr = list(map(int, input().split()))
#    ccc = [0 for _ in range(V+1)]
#    ans = []
#    cnt = 0
#    for i in range(0, len(arr), 2):
#        nxn[arr[i]][arr[i+1]] = 1
#    for i in range(1, len(arr), 2):
#        ccc[arr[i]] += 1
#    while 1:
#        for i in range(1, V+1):
#            if ccc[i] == 0:
#                ans.append(i)
#                ccc[i] = -1
#                dfs(i)
#        cnt = ccc.count(-1)
#        if cnt == V:
#            break
#    print("#%d" % (test+1), end=" ")
#    for i in range(V):
#        print(ans[i], end=" ")
#    print()