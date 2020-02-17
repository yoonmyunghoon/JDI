import sys
sys.stdin = open("출근하는브라운.txt")

N = int(input())
subway = list(map(int, input().split()))
result = 0
s = 0
e = N-1
Max = 0
count1 = 0
count2 = 0
while subway[s] == 0:
    count1 += 1
    s += 1
while subway[e] == 0:
    count2 += 1
    e -= 1
while s < e:
    dis = 1
    while subway[s] != 1:
        s += 1
        dis += 1
        if Max < dis:
            Max = dis
        if s == e:
            break
    else:
        s += 1

if Max%2==0:
    result = Max//2
else:
    result = Max//2+1
print(max(count1, count2, result))


