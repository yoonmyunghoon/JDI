def solution(number, k):
    stack = []
    for i in range(len(number)):
        if k == 0:
            break
        if len(stack) == 0:
            stack.append(number[i])
        else:
            while 1:
                if k == 0:
                    stack.append(number[i:])
                    break
                if len(stack) == 0:
                    stack.append(number[i])
                    break
                elif stack[-1] >= number[i]:
                    stack.append(number[i])
                    break
                else:
                    stack.pop()
                    k -= 1
    print(stack)
    answer = ''.join(stack)
    return answer


N = "777000"
K = 2
print(solution(N, K))



