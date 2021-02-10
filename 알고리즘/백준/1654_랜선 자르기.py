import sys
sys.stdin = open("1654_랜선 자르기.txt")
input = sys.stdin.readline


def find_length(s, e):
    while s <= e:
        mid = (s+e)//2
        all_cnt = 0
        for Line in LAN_Lines:
            cnt = Line//mid
            all_cnt += cnt
        if all_cnt < N:
            e = mid - 1
        else:
            s = mid + 1
    return e


K, N = map(int, input().split())
LAN_Lines = [int(input()) for _ in range(K)]
Max_length = max(LAN_Lines)
print(find_length(1, Max_length))

