def solution(a):
    answer = 0
    if len(a) < 3:
        answer = len(a)
    else:
        for i in range(1, len(a)-1):
            check = 0
            x1 = i
            x2 = i
            while 1:
                x1 -= 1
                if a[x1] < a[i]:
                    check += 1
                    break
                if x1 == 0:
                    break
            while 1:
                x2 += 1
                if a[x2] < a[i]:
                    check += 1
                    break
                if x2 == len(a)-1:
                    break
            if check == 2:
                answer += 1
        answer = len(a) - answer
    return answer

print(solution([9,-1,-5]))