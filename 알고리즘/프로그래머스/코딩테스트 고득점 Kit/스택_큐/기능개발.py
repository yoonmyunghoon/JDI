def solution(progresses, speeds):
    answer = []
    top = 0
    date = 0
    while 1:
        if top == len(progresses):
            break
        while 1:
            date += 1
            if progresses[top] + speeds[top]*date >= 100:
                break
        cnt = 0
        while 1:
            if top == len(progresses):
                break
            if progresses[top] + speeds[top]*date >= 100:
                cnt += 1
                top += 1
            else:
                break
        answer.append(cnt)
    return answer


P = [95, 90, 99, 99, 80, 99]
S = [1, 1, 1, 1, 1, 1]
print(solution(P, S))