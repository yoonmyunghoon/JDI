import sys, collections
sys.stdin = open("2606_바이러스.txt")

def bfs(x):
    visited[x] = 1
    deq = collections.deque()
    deq.append(x)
    cnt = 0
    while deq:
        t = deq.popleft()
        cnt += 1
        for i in range(n):
            if G[t][i] == 1 and visited[i] == 0:
                visited[i] = 1
                deq.append(i)
    return cnt-1

n = int(input())
m = int(input())
G = [[0 for _ in range(n)] for _ in range(n)]
visited = [0]*n
for i in range(m):
    a, b = map(int, input().split())
    G[a-1][b-1] = 1
    G[b-1][a-1] = 1
print(bfs(0))