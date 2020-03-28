import sys
sys.stdin = open("10844_쉬운 계단 수.txt")

N = int(input())
check1 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
check2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(2, N+1):
    if i % 2 == 0:
        check2[0] = check1[1]
        check2[9] = check1[8]
        for j in range(1, 9):
            check2[j] = check1[j-1] + check1[j+1]
    else:
        check1[0] = check2[1]
        check1[9] = check2[8]
        for j in range(1, 9):
            check1[j] = check2[j - 1] + check2[j + 1]
if N % 2 == 0:
    print(sum(check2)%1000000000)
else:
    print(sum(check1)%1000000000)