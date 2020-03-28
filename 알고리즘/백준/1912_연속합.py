import sys
sys.stdin = open("1912_연속합.txt")

n = int(input())
info = list(map(int, input().split()))
info = [0] + info
tmp = [0] * (n+1)
maximum = info[1]
for i in range(1, n+1):
    tmp[i] = max(tmp[i-1]+info[i], info[i])
    maximum = max(tmp[i], maximum)
print(maximum)