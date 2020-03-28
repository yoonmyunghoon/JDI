
def solution(stones, k):
    answer = 0
    zeros = [1]*len(stones)
    stones_set = set(stones)
    stones_set = list(stones_set)
    stones_set.sort()
    num = 0
    flag = 0
    while 1:
        if flag == 1:
            break
        for i in range(len(stones)):
            if zeros[i] == 1:
                if stones_set[num] >= stones[i]:
                    zeros[i] = 0
        maxsuscnt = 0
        suscnt = 0
        for i in range(len(zeros)):
            if zeros[i] == 0:
                suscnt += 1
            if zeros[i] == 1:
                if maxsuscnt < suscnt:
                    maxsuscnt = suscnt
                    suscnt = 0
                    if maxsuscnt >= k:
                        flag = 1
                        break
        num += 1
    answer = stones_set[num-1]
    return answer
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))