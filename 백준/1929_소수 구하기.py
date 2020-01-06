import sys
sys.stdin = open("1929_소수 구하기.txt")

M, N = map(int, input().split())
for i in range(M, N+1):
    if i == 1:
        continue
    if i == 2:
        print(2)
        continue
    if i % 2 == 0:
        continue
    for j in range(2, int((i)**(0.5))+1):
        if i%j == 0:
            break
    else:
        print(i)