import sys
sys.stdin = open('3079_입국심사.txt')
# input = sys.stdin.readline


def find_min_time(start, end):
    while start < end:
        passed_person_cnt = 0
        mid = (start + end) // 2
        for t in judge_times:
            passed_person_cnt += mid//t
        if passed_person_cnt < M:
            start = mid + 1
        else:
            end = mid
    return end


N, M = map(int, input().split())
judge_times = [int(input()) for _ in range(N)]
len_of_list = len(judge_times)
max_of_time = max(judge_times)
print(find_min_time(1, (M//N+1)*max_of_time))


