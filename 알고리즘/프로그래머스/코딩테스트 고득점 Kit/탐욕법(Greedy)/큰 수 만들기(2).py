def solution(number, k):
    stack = []
    for i in range(len(number)):
        if k == 0:
            break
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
    if k != 0:
        answer = ''.join(stack[:-k])
    else:
        answer = ''.join(stack)
    return answer


N = "4177252841"
K = 4
print(solution(N, K))



