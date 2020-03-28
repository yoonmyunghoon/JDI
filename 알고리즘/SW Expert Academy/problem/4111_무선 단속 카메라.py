import sys
sys.stdin = open("4111_무선 단속 카메라.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    K = int(input())
    kameras = list(map(int, input().split()))
    if N <= K:
        print('#{} {}'.format(tc, 0))
    else:
        kameras = set(kameras)
        kameras = list(kameras)
        kameras.sort()
        difer = []
        for i in range(len(kameras)-1):
            difer.append(kameras[i+1]-kameras[i])
        difer.sort()
        count = len(difer) - (K-1)
        result = 0
        for i in range(count):
            result += difer[i]
        print('#{} {}'.format(tc, result))
