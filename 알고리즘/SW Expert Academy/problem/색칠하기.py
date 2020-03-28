import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(N):
        lis = list(map(int, input().split()))
        if lis[4] == 1:
            for x in range(lis[0], lis[2]+1):
                for y in range(lis[1], lis[3]+1):
                    if data[x][y] == 2:
                        data[x][y] += 1
                    else:
                        data[x][y] = 1
        if lis[4] == 2:
            for x in range(lis[0], lis[2]+1):
                for y in range(lis[1], lis[3]+1):
                    if data[x][y] == 1:
                        data[x][y] += 2
                    else:
                        data[x][y] = 2
    count = 0
    for i in range(10):
        for j in range(10):
            if data[i][j] == 3:
                count += 1
    print('#{} {}'.format(tc, count))

