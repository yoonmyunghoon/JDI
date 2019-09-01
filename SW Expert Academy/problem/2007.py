import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    arr = input()
    count = 1
    while arr[0:count] != arr[count:2*count]:
        count += 1
    print('#{} {}'.format(tc, count))

