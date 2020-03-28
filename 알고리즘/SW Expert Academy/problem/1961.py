import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(G[N - j - 1][i], end='')
        print(' ', end='')
        for k in range(N):
            print(G[N - i - 1][N - k - 1], end='')
        print(' ', end='')
        for l in range(N):
            print(G[l][N-i-1], end='')
        print()