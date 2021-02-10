import sys
sys.stdin = open("2512_예산.txt")


def find_asset():
    s = 0
    e = M
    while s <= e:
        mid = (s+e)//2
        all_asset = 0
        for a in A:
            if a <= mid:
                all_asset += a
            else:
                all_asset += mid
        if all_asset == M:
            return mid
        elif all_asset < M:
            s = mid + 1
        else:
            e = mid - 1
    return e


N = int(input())
A = list(map(int, input().split()))
M = int(input())
if sum(A) <= M:
    print(max(A))
else:
    print(find_asset())