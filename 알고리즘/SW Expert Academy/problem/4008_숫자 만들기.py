import sys
sys.stdin = open('4008_숫자 만들기.txt')


def cal(d, result):
    global maximum, minimum
    if d == N:
        if result > maximum:
            maximum = result
        if result < minimum:
            minimum = result
        return
    else:
        if operations[0] != 0:
            operations[0] -= 1
            cal(d+1, result+numbers[d])
            operations[0] += 1
        if operations[1] != 0:
            operations[1] -= 1
            cal(d+1, result-numbers[d])
            operations[1] += 1
        if operations[2] != 0:
            operations[2] -= 1
            cal(d+1, result*numbers[d])
            operations[2] += 1
        if operations[3] != 0:
            operations[3] -= 1
            cal(d+1, int(result/numbers[d]))
            operations[3] += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    operations = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    maximum = -987654321
    minimum = 987654321
    cal(1, numbers[0])
    print('#{} {}'.format(tc, maximum-minimum))