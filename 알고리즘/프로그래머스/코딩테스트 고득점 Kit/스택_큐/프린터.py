def solution(priorities, location):
    length = len(priorities)
    check = [0]*length
    now_max = max(priorities)
    prior_check = [0]*10
    for p in priorities:
        prior_check[p] += 1

    cnt = 0
    idx = 0
    while 1:
        if cnt == length:
            break
        if check[idx] == 0:
            if priorities[idx] == now_max:
                cnt += 1
                check[idx] = cnt
                if cnt == length:
                    break
                prior_check[now_max] -= 1
                while 1:
                    if prior_check[now_max] != 0:
                        break
                    now_max -= 1
        idx += 1
        idx %= length
    return check[location]


ex_priorities = [2, 1, 3, 2]
ex_location = 2
print(solution(ex_priorities, ex_location))

