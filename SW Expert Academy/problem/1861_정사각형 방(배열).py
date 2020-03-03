import sys
sys.stdin = open('1861_정사각형 방(n1000).txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*(N*N+1)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<N and 0<=ny<N and A[i][j] + 1 == A[nx][ny]:
                    v[A[i][j]] = 1
                    break
    maximum = 0
    minimumnum = 987654321
    cnt = 0
    for i in range(N*N, -1, -1):
        if v[i] == 1:
            cnt += 1
        else:
            if maximum <= cnt:
                maximum = cnt
                minimumnum = i
            cnt = 0

    print('#{} {} {}'.format(tc, minimumnum+1, maximum+1))
