import sys
sys.stdin = open("5656. [모의 SW 역량테스트] 벽돌 깨기.txt")

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    # print(N, W, H)
    G = [list(map(int, input().split())) for _ in range(H)]
    # for i in G:
    #     print(i)
    # print()
    while 1:
        if N == 0:
            break
        for w in range(W):
            h = 0
            while 1:
                if G[h][w] == 1:
                    break
                elif h == H:
                    h = -1
                    break
                else:
                    h += 1
            if h != -1:
                N -= 1



