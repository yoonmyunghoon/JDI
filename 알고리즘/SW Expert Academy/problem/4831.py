T = int(input())
numofcharge = []
for i in range(T):
    numofcharge.append(0)
for test_case in range(T):
    K, N, M = map(int, input().split())
    charge = input().split(' ')
    w = K
    for i in range(M):
        if i < M-1:
            if int(charge[i]) < K:
                if int(charge[i+1]) > K:
                    numofcharge[test_case] += 1
                    K = int(charge[i]) + w
            elif int(charge[i]) == K:
                numofcharge[test_case] += 1
                K = int(charge[i]) + w
            else:
                numofcharge[test_case] = 0
                break
        else:
            if K < N:
                if int(charge[i]) + w >= N:
                    numofcharge[test_case] += 1
                else:
                    numofcharge[test_case] = 0

for i, x in enumerate(numofcharge):
    print('#{} {}'.format(i+1, x))