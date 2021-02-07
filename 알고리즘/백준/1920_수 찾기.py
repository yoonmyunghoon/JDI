import sys
sys.stdin = open("1920_수 찾기.txt")

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()
for i in range(len(B)):
    s = 0
    e = len(A) - 1
    flag = 0
    while s <= e:
        mid = (s+e)//2
        if B[i] == A[mid]:
            flag = 1
            break
        elif B[i] < A[mid]:
            e = mid - 1
        else:
            s = mid + 1
    if flag == 1:
        print(1)
    else:
        print(0)