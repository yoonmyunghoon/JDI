
def solution(a):
    if len(a) < 3:
        return len(a)
    answer = 0
    before = 0
    min_check = a[0]
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            temp = max(min_check, a[i])
            for j in range(before, i):
                if a[j] > temp:
                    answer += 1
            before = i
            min_check = min(min_check, a[i])
    return len(a) - answer

print(solution([9,-1,-5]))