def solution(number, k):
    answer = []
    length = len(number)
    cnt = k
    idx = 0
    while 1:
        if cnt == 0:
            break
        else:
            flag = 0
            for i in range(1, cnt+1):
                if idx+i >= length:
                    flag = 2
                    break
                if number[idx] < number[idx+i]:
                    cnt -= i
                    flag = 1
                    idx += i
                    break
            if flag == 2:
                return ''.join(answer)
            if flag == 0:
                answer.append(number[idx])
                idx += 1
    return ''.join(answer) + number[idx:]


N = "777000"
K = 2
print(solution(N, K))



