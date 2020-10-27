def solution(n, lost, reserve):
    check = [1]*(n+1)
    for l in lost:
        check[l] -= 1
    for r in reserve:
        check[r] += 1
    for i in range(1, n):
        if check[i] == 2:
            if check[i-1] == 0:
                check[i] = 1
                check[i-1] = 1
            elif check[i+1] == 0:
                check[i+1] = 1
                check[i] = 1
    if check[-1] == 2:
        if check[-2] == 0:
            check[-1] = 1
            check[-2] = 1
    answer = n-check[1:].count(0)
    return answer


N = 5
L = [2, 4]
R = [1, 3, 5]
print(solution(N, L, R))


