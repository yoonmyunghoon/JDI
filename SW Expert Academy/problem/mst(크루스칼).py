import sys
sys.stdin = open("mst.txt")

def findset(x):
    if x == PI[x]: return x
    else: return findset(PI[x])

def union(x, y):
    PI[findset(y)] = findset(x)


def mst():
    global V
    N = 0
    k = 0
    total = 0
    while N < V-1:
        if findset(G_E[k][0]) != findset(G_E[k][1]):
            union(G_E[k][0], G_E[k][1])
            total += G_E[k][2]
            N += 1
        k += 1
    return total

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G_E = []
    PI = list(range(V+1))
    for i in range(E):
        n1, n2, w = map(int, input().split())
        G_E.append([n1, n2, w])
    G_E.sort(key=lambda x: x[2])
    print('#{} {}'.format(tc, mst()))