def solution(citations):
    citations.sort(reverse=True)
    h = citations[0]
    if h == 1:
        return 1
    if citations[0] == citations[-1]:
        return min(len(citations), citations[0])
    flag = 0
    for i in range(len(citations)):
        if flag == 1:
            break
        if citations[i] != h:
            while 1:
                h -= 1
                if citations[i] == h:
                    if h <= i+1:
                        flag = 1
                    break
                else:
                    if h <= i:
                        flag = 1
                        break
    if h > len(citations):
        return len(citations)
    else:
        return h


C = [0]
print(solution(C))