import sys
sys.stdin = open("베이비진 게임.txt")

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))

    p1 = []
    p2 = []
    sp1 = []
    sp2 = []
    for i in range(6):
        p1.append(data.pop(0))
        p2.append(data.pop(0))

        if i >= 2:
            sp1 = sorted(p1)
            sp2 = sorted(p2)
            print(sp1)
            print(sp2)

    # print(p1)
    # print(p2)