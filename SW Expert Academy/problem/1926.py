import sys
sys.stdin = open("input.txt")

N = int(input())
data = list(map(str, range(1, N+1)))
for i in range(len(data)):
    count = 0
    for j in data[i]:
        if j in '369':
            count += 1
    if count > 0:
        data[i] = '-'*count

print(' '.join(data))




