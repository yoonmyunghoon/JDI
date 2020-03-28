import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    waper = [list(map(int, input().split())) for _ in range(H)]
    # for i in waper:
    #     print(i)
    # print()
