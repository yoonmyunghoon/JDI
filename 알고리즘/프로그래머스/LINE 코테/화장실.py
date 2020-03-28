import sys
sys.stdin = open("화장실.txt")

Time = [0]*150
N = int(input())
for i in range(N):
    s, e = map(int, input().split())
    for j in range(s, e):
        Time[j] += 1
print(max(Time))
