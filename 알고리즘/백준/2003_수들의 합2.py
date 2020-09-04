import sys
sys.stdin = open("2003_수들의 합2.txt")


def counting(s, e, m):
    count = 0
    sum_of_num = 0
    while 1:
        if sum_of_num >= m:
            sum_of_num -= A[s]
            s += 1
        elif e == N:
            break
        else:
            sum_of_num += A[e]
            e += 1
        if sum_of_num == m:
            count += 1
    return count


N, M = map(int, input().split())
A = list(map(int, input().split()))
print(counting(0, 0, M))