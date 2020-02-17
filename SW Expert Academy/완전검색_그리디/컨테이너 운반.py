import sys
sys.stdin = open("컨테이너 운반.txt")


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    # print(container)
    # print(truck)
    weight = 0
    while 1:
        if sum(container) == 0 or sum(truck) == 0:
            break
        for i in range(len(truck)):
            for j in range(len(container)):
                if container[j] != 0:
                    if truck[i] >= container[j]:
                        weight += container[j]
                        truck[i] = 0
                        container[j] = 0
                        break
                    else:
                        container[j] = 0
    print('#{} {}'.format(tc, weight))