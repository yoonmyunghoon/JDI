import sys
sys.stdin = open("2343_기타 레슨.txt")
# input = sys.stdin.readline


def find_size(start, end):
    min_bluelay_len = end
    while start <= end:
        mid = (start+end)//2
        size = 0
        lessons_len = 0
        flag = 0
        for lesson in lesson_list:
            if lesson > mid:
                flag = 1
                break
            if lessons_len == 0:
                size += 1
            if lessons_len + lesson > mid:
                lessons_len = lesson
                size += 1
            elif lessons_len + lesson < mid:
                lessons_len += lesson
            else:
                lessons_len = 0
        if flag == 1:
            start = mid + 1
        else:
            # print(start, mid, end, size)
            if size > M:
                start = mid + 1
            else:
                if min_bluelay_len > mid:
                    min_bluelay_len = mid
                end = mid
        if start == end:
            return min_bluelay_len


N, M = map(int, input().split())
lesson_list = list(map(int, input().split()))
print(find_size(1, sum(lesson_list)))


