def solution(n):
    result = []
    while 1:
        if n == 0:
            break
        result.append(n%3)
        n = n // 3
    answer = 0
    for i in range(len(result)-1, -1, -1):
        answer += result[i]*(3**(len(result)-i-1))
    return answer

print(solution(125))