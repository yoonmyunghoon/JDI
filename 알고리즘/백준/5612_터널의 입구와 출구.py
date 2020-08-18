import sys
sys.stdin = open("5612_터널의 입구와 출구.txt")

n = int(input())
m = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
maximum = 0
s = m
check = 1

for a, b in info:
    s = s + a - b
    if s < 0:
        check = 0
        break
    else:
        if s > maximum:
            maximum = s
if check:
    print(maximum)
else:
    print(0)
