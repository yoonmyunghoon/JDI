def solution(number, k):
    answer = []
    length = len(number)
    check = [1]*length
    cnt = k
    idx = 0
    while 1:
        if cnt == 0:
            break
        else:
            flag = 0
            for i in range(1, cnt+1):
                if idx+i >= length:
                    for j in range(idx, length):
                        check[j] = 0
                        flag = 2
                    break
                if number[idx] < number[idx+i]:
                    for j in range(i):
                        check[idx+j] = 0
                    cnt -= i
                    flag = 1
                    idx += i
                    break
            if flag == 2:
                break
            if flag == 0:
                idx += 1
    for i in range(length):
        if check[i] == 1:
            answer.append(number[i])
    return ''.join(answer)


N = "777707022"
K = 1
print(solution(N, K))



