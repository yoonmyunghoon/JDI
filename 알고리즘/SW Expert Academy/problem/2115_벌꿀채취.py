import sys
sys.stdin = open("2115_벌꿀채취.txt")

def powerSet(n, k, a, b):
    global maximum, maxposition
    if n == k:
        hap = 0
        hap1 = 0
        for t in range(n):
            if A[t] == 1:
                hap += arr[t]
        if hap <= C:
            for t in range(n):
                if A[t] == 1:
                    hap1 += arr[t] * arr[t]
            if maximum < hap1:
                maximum = hap1
                maxposition = [a, b]
    else:
        A[k] = 1
        powerSet(n, k+1, a, b)
        A[k] = 0
        powerSet(n, k+1, a, b)

def powerSet1(n, k):
    global maximum1
    if n == k:
        hap = 0
        hap1 = 0
        for t in range(n):
            if A[t] == 1:
                hap += arr[t]
        if hap <= C:
            for t in range(n):
                if A[t] == 1:
                    hap1 += arr[t] * arr[t]
            if maximum1 < hap1:
                maximum1 = hap1
    else:
        A[k] = 1
        powerSet1(n, k+1)
        A[k] = 0
        powerSet1(n, k+1)


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    bultongs = [list(map(int, input().split())) for _ in range(N)]
    maximum = 0
    maxposition = [0, 0]
    for i in range(N):
        for j in range(N-M+1):
            arr = []
            for k in range(M):
                arr.append(bultongs[i][j+k])
            if sum(arr) <= C:
                hap = 0
                for q in range(len(arr)):
                    hap += arr[q]*arr[q]
                if maximum < hap:
                    maximum = hap
                    maxposition = [i, j]
            else:
                A = [0] * M
                powerSet(M, 0, i, j)

    for i in range(maxposition[1]-M+1, maxposition[1]+M-1+M):
        if i < 0 or i >= N:
            continue
        else:
            bultongs[maxposition[0]][i] = 0
    maximum1 = 0
    for i in range(N):
        for j in range(N-M+1):
            if bultongs[i][j] != 0:
                arr = []
                hap = 0
                for k in range(M):
                    arr.append(bultongs[i][j+k])
                if sum(arr) <= C:
                    for q in range(len(arr)):
                        hap += arr[q]*arr[q]
                    if maximum1 < hap:
                        maximum1 = hap
                else:
                    A = [0] * M
                    powerSet1(M, 0)

    print('#{} {}'.format(tc, maximum+maximum1))





