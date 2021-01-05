import sys
sys.stdin = open("1182_부분수열의 합.txt")


def checking(depth, current_sum, count):
    global cnt
    if depth == N:
        if current_sum == S and count > 0:
            cnt += 1
        return
    checking(depth + 1, current_sum, count)
    checking(depth + 1, current_sum+data[depth], count+1)


N, S = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0
checking(0, 0, 0)
print(cnt)