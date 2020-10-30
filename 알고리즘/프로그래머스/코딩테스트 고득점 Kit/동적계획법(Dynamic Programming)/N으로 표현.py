def solution(N, number):
    calc = [[] for _ in range(9)]
    if N == number:
        return 1
    calc[1].append(N)
    for i in range(2, 9):
        if calc[i-1][0]*10+N == number:
            return i
        else:
            calc[i].append(calc[i-1][0]*10+N)
        for j in range(1, i):
            for num_1 in calc[j]:
                for num_2 in calc[i-j]:
                    temp = num_1 + num_2
                    if temp == number:
                        return i
                    else:
                        calc[i].append(temp)
                    temp = num_1 - num_2
                    if temp == number:
                        return i
                    else:
                        calc[i].append(temp)
                    temp = num_1 * num_2
                    if temp == number:
                        return i
                    else:
                        calc[i].append(temp)
                    if num_2 == 0:
                        continue
                    temp = num_1 // num_2
                    if temp == number:
                        return i
                    else:
                        calc[i].append(temp)
    return -1


ex_N = 2
ex_number = 11
print(solution(ex_N, ex_number))
