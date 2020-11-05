def solution(s):
    answer = []
    change_cnt = 0
    zero_cnt = 0

    while 1:
        if s == "1":
            break
        length = len(s)
        temp = 0
        for i in range(length):
            if s[i] == "0":
                temp += 1
        zero_cnt += temp
        result = length - temp
        changed = []
        while 1:
            if result == 1:
                changed.append(1)
                break
            changed.append(result % 2)
            result = result // 2
        changed.reverse()
        s = "".join(map(str, changed))
        change_cnt += 1
    answer.append(change_cnt)
    answer.append(zero_cnt)
    return answer


a = "110010101001"
print(solution(a))