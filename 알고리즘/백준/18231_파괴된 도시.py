import sys
sys.stdin = open("18231_파괴된 도시.txt")

N, M = map(int, input().split())
G = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):
    U, V = map(int, input().split())
    G[U-1][V-1] = 1
    G[V-1][U-1] = 1
K = int(input())
# 파괴된 도시들
destroyed = list(map(int, input().split()))
# 미사일을 맞았다고 가정할 도시들
result = []
# 주위에 전부 파괴되어있을 경우에 result에 넣음
for i in range(len(destroyed)):
    check = 0
    for j in range(N):
        if G[destroyed[i]-1][j] == 1:
            if j+1 not in destroyed:
                check = 1
                break
    if check == 0:
        result.append(destroyed[i])

# 미사일을 맞았다고 가정한 도시들을 통해 주위에 도시들을 다 파괴함
compare = []
for i in range(len(result)):
    compare.append(result[i])
    for j in range(N):
        if G[result[i]-1][j] == 1:
            compare.append(j+1)

compare = set(compare)
compare = list(compare)
compare.sort()
destroyed.sort()
length = len(result)
if length == 0 or compare != destroyed:
    print(-1)
else:
    result.sort()
    print(length)
    for i in result:
        print(i, end=' ')