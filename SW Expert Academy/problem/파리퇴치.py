import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for x in range(M):
                for y in range(M):
                    sum += data[i+x][j+y]
            # for x in range(M-2):
            #     for y in range(M-2):
            #         sum -= data[i+1+x][j+1+y]
            if sum > max:
                max = sum
    print('#{} {}'.format(tc, max))


