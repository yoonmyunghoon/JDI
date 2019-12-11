import sys
sys.stdin = open('5432_쇠막대기 자르기.txt')

T = int(input())
for tc in range(1, T+1):
    pipes = list(input())
    result = 0
    num = 0
    switch = 0
    for i in range(len(pipes)):
        if pipes[i] == '(':
            if switch == 1: num += 1
            else: switch = 1
        else:
            if pipes[i-1] == '(':
                result += num
                switch = 0
            else:
                num -= 1
                result += 1
    print('#{} {}'.format(tc, result))