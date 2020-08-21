import sys
sys.stdin = open("11724_연결 요소의 개수.txt")


# Union-Find
def find(n):
    if p[n] < 0:
        return n
    else:
        p[n] = find(p[n])
        return p[n]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    else:
        p[b] = a


N, M = map(int, input().split())
p = [-1] * (N+1)
for i in range(M):
    u, v = map(int, input().split())
    union(u, v)

result = set()
for i in range(1, N+1):
    result.add(find(i))
print(len(result))
