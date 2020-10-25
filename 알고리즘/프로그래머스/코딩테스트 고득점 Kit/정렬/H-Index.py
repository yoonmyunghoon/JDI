def solution(citations):
    citations.sort(reverse=True)
    h = 1
    if len(citations) == 1:
        return 1
    if citations[0] == citations[-1]:
        return min(len(citations), citations[0])
    while h <= len(citations) and h <= citations[h-1]:
        h += 1
    return h-1

citations = [0]

print(solution(citations))
