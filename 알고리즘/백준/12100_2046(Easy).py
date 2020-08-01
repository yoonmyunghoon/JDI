import sys
sys.stdin = open("12100_2046(Easy).txt")

N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]
print(N)
for i in blocks:
    print(i)
