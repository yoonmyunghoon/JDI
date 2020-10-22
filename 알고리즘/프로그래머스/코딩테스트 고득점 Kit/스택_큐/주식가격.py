def solution(prices):
    l = len(prices)
    answer = [0] * l
    stack = []
    for i in range(l):
        if len(stack) == 0:
            stack.append([prices[i], i])
        else:
            while 1:
                if len(stack) == 0:
                    stack.append([prices[i], i])
                    break
                else:
                    if stack[-1][0] > prices[i]:
                        t = stack.pop()
                        answer[t[1]] = i - t[1]
                    else:
                        stack.append([prices[i], i])
                        break
    for i in range(len(stack)):
        answer[stack[i][1]] = l - stack[i][1] - 1
    return answer


P = [3, 5, 2, 5, 2]
print(solution(P))

# 3 5 2 5 2
# 2 1 2 1 0
#
#
# 2 2, 2 4



