import sys
sys.stdin = open("2096_내려가기.txt")

N = int(input())
max_list = list(map(int, input().split()))
min_list = max_list
for i in range(N-1):
    now_list = list(map(int, input().split()))
    max_a = max(max_list[0]+now_list[0], max_list[1]+now_list[0])
    max_b = max(max_list[0]+now_list[1], max_list[1]+now_list[1], max_list[2]+now_list[1])
    max_c = max(max_list[1]+now_list[2], max_list[2]+now_list[2])
    max_list = [max_a, max_b, max_c]
    min_a = min(min_list[0] + now_list[0], min_list[1] + now_list[0])
    min_b = min(min_list[0] + now_list[1], min_list[1] + now_list[1], min_list[2] + now_list[1])
    min_c = min(min_list[1] + now_list[2], min_list[2] + now_list[2])
    min_list = [min_a, min_b, min_c]
print(max(max_list), min(min_list))


