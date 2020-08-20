import sys
sys.stdin = open("5671_호텔 방 번호.txt")


def d_check(num):
    s_num = str(num)
    data = []
    for i in range(len(s_num)):
        data.append(s_num[i])
    if len(data) != len(set(data)):
        return 0
    else:
        return 1


while 1:
    try:
        N, M = map(int, input().split())
        cnt = 0
        for number in range(N, M+1):
            cnt += d_check(number)
        print(cnt)
    except EOFError:
        break