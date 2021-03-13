import sys
sys.stdin = open('1300_K번째 수.txt')
# input = sys.stdin.readline


def find_index(start, end):
    while start < end:
        mid = (start+end)//2
        cnt = 0
        for i in range(1, N+1):
            cnt += min(N, mid//i)
        if cnt < k:
            start = mid + 1
        else:
            end = mid
    return end


N = int(input())
k = int(input())
print(find_index(1, N**2))