import sys
sys.stdin = open("6236_용돈 관리.txt")
input = sys.stdin.readline


def find_min_money(s, e):
    result = e
    while s <= e:
        mid = (s+e)//2
        m = 1
        k = mid
        for money in Money:
            if money <= k:
                k -= money
            else:
                m += 1
                k = mid - money
        if m <= M:
            if result > mid:
                result = mid
            e = mid - 1
        else:
            s = mid + 1
    return result


N, M = map(int, input().split())
Money = [int(input()) for _ in range(N)]
Max = max(Money)
print(find_min_money(Max, Max*N))