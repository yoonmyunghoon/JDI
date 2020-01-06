import sys
sys.stdin = open("1010_다리놓기.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[0 for _ in range(M+1)] for _ in range(M+1)]
    for i in range(M+1):
        for j in range(M+1):
            if i == j:
                G[i][j] = 1
            elif j == 0:
                G[i][j] = 1
            else:
                G[i][j] = G[i-1][j-1] + G[i-1][j]
    print(G[M][N])