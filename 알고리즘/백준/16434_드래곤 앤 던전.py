import sys
sys.stdin = open('16434_드래곤 앤 던전.txt')


# def find_HP(start, end):
#     while start < end:
#         mid = (start+end)//2
#         for i in range(N):
#             if room[0] == 1: # 몬스터
#
#             else: # 포션



N, A = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
print(N, A)
print(room)
# print(find_HP(1, 123456*1000000))
