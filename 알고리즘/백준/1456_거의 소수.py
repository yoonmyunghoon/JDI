import sys
sys.stdin = open("1456_거의 소수.txt")

A, B = map(int, input().split())
s_A = int(A**0.5)
s_B = int(B**0.5)
data = [1] * (s_B+1)
data[0] = 0
data[1] = 0
for i in range(4, s_B+1, 2):
    data[i] = 0
for i in range(3, int(s_B**0.5)+1, 2):
    if data[i]:
        for j in range(i*i, s_B+1, 2*i):
            data[j] = 0
cnt = 0
for i in range(2, s_B+1):
    if data[i]:
        n = 2
        while 1:
            if i**n > B:
                break
            if A <= i**n <= B:
                cnt += 1
            n += 1
print(cnt)