def solution(N, number):
    calc = [[] for _ in range(8)]
    if N == number:
        return 1
    calc[0].append(N)
    print(calc)
    # for i in range(1, 8):
    #     if calc[i-1]*10+N == number:
    #         return i+1
    #     for j in range(len(calc[i-1])):
    #         if

    return -1


ex_N = 5
ex_number = 12
print(solution(ex_N, ex_number))
