def solution(n, lost, reserve):
    check = [1]*(n+1)
    for l in lost:
        check[l] -= 1
    for r in reserve:
        check[r] += 1
    for i in range(1, n+1):
        if check[i] == 2:
            if i == n:
                if check[i-1] == 0:
                    check[i-1] = 1
                    check[i] = 1
            else:
                if check[i-1] == 0 or check[i+1] == 0:
                    if check[i-1] + check[i+1] != 0:
                        if check[i-1] == 0:
                            check[i-1] = 1
                            check[i] = 1
                        else:
                            check[i + 1] = 1
                            check[i] = 1
    for i in range(1, n+1):
        if check[i] == 0:
            if i == n:
                if check[i-1] == 2:
                    check[i-1] = 1
                    check[i] = 1
            else:
                if check[i-1] == 2 or check[i+1] == 2:
                    if check[i-1] == 2:
                        check[i-1] = 1
                        check[i] = 1
                    else:
                        check[i + 1] = 1
                        check[i] = 1
    answer = n - check[1:].count(0)
    return answer

N = 3
L = [3]
R = [1]
print(solution(N, L, R))


