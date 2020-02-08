import sys, collections
sys.stdin = open("1043_거짓말.txt")

def bfs(x):
    visited[x] = 1
    deq = collections.deque()
    deq.append(x)
    while deq:
        t = deq.popleft()
        for i in range(N):
            if G[t][i] == 1 and visited[i] == 0:
                visited[i] = 1
                deq.append(i)

N, M = map(int, input().split())
G = [[0 for _ in range(N)] for _ in range(N)]
iknow = list(map(int, input().split()))
parties = []
visited = [0]*N
for i in range(M):
    party = list(map(int, input().split()))
    a = party.pop(0)
    party.sort()
    party.insert(0, a)
    parties.append(party)
if iknow[0] == 0:
    print(M)
else:
    for i in range(M):
        for j in range(1, parties[i][0]):
            for k in range(j+1, parties[i][0]+1):
                G[parties[i][j]-1][parties[i][k]-1] = 1
    for i in range(N-1):
        for j in range(i+1, N):
            G[j][i] = G[i][j]
    iknow.pop(0)
    iknow.sort()
    for i in range(len(iknow)):
        if visited[iknow[i]-1] == 0:
            bfs(iknow[i]-1)
    cnt = M
    A = []
    for i in range(len(visited)):
        if visited[i] == 1:
            A.append(i+1)
    # print(A)
    for j in range(M):
        for k in range(1, parties[j][0]+1):
            if parties[j][k] in A:
                cnt -= 1
                break
    print(cnt)

