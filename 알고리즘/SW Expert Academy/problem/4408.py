import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    rooms = [0] * 401
    for i in range(N):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        if a%2 == 0:
            a = a-1
        if b%2 == 1:
            b = b+1
        for j in range(a, b+1):
            rooms[j] += 1
    print('#{} {}'.format(tc, max(rooms)))

