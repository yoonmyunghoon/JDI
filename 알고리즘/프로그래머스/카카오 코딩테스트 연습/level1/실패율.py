def solution(N, stages):
    answer = []
    passed = [0]*(N+2)
    ended = [0]*(N+2)
    for stage in stages:
        ended[stage] += 1
        for i in range(1, stage+1):
            passed[i] += 1
    for k in range(1, N+1):
        failure = 0
        if passed[k] != 0:
            failure = ended[k]/passed[k]
        answer.append([failure, k])
    answer.sort(key=lambda x: (-x[0], x[1]))
    result = list(map(lambda x: x[1], answer))
    return result


N_ex = 5
stages_ex = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N_ex, stages_ex))