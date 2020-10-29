def solution(name):
    answer = 0
    result = []
    for i in range(len(name)):
        n = ord(name[i])-64
        result.append(min(n-1, 27-n))
    idx = 0
    while 1:
        answer += result[idx]
        result[idx] = 0
        if sum(result) == 0:
            break
        left_idx = idx
        left_cnt = 0
        right_idx = idx
        right_cnt = 0
        while 1:
            left_idx -= 1
            left_cnt += 1
            if result[left_idx] != 0:
                break
        while 1:
            right_idx += 1
            right_cnt += 1
            if result[right_idx] != 0:
                break
        if left_cnt < right_cnt:
            answer += left_cnt
            idx = left_idx
        else:
            answer += right_cnt
            idx = right_idx
    return answer


N = "BBABAAAB"
print(solution(N))
