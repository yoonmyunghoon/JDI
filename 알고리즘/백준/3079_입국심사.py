import sys
sys.stdin = open('3079_입국심사.txt')
# input = sys.stdin.readline


def find_time(start, end):
    time = 0
    list_len = len(judge_times)
    while start < end:
        mid = (start + end) // 2
        min_value = 10**9
        min_index = 0
        for i in range(list_len):
            if judge_times[i] < min_value:
                min_index = i
        time = judge_times[i]
        judge_times[i] += judge_times[i]



N, M = map(int, input().split())
judge_times = [int(input()) for _ in range(N)]
print(N, M, judge_times)
find_time(1, (M//N+1)*max(judge_times))


