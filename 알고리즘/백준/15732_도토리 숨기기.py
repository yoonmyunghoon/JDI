import sys
sys.stdin = open('15732_도토리 숨기기.txt')
input = sys.stdin.readline


def find_last_box(start, end):
    while start < end:
        mid = (start+end)//2
        cnt = 0
        for A, B, C in data:
            limit = min(B, mid)
            if A <= limit:
                cnt += (limit-A)//C + 1
        if cnt < D:
            start = mid+1
        else:
            end = mid
    return end


N, K, D = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(K)]
print(find_last_box(1, N))




