import sys
sys.stdin = open("17825_주사위 윷놀이.txt")

dice = list(map(int, input().split()))
score = [
    [i for i in range(0, 41, 2)],
    [10, 13, 16, 19, 25, 30, 35, 40],
    [20, 22, 24],
    [30, 28, 27, 26]
]
answer = 0


def dfs(k, pos, total):
    global answer
    if k == 10:
        if total > answer:
            answer = total
    else:
        for i in range(4):
            tt = [a[:] for a in pos]
            ttotal = total
            tpos = tt[i]
            if tpos[1] < 0:
                continue
            tpos[1] += dice[k]

            if tpos[0] == 0:
                if tpos[1] == 5:
                    tpos[0], tpos[1] = 1, 0
                elif tpos[1] == 10:
                    tpos[0], tpos[1] = 2, 0
                elif tpos[1] == 15:
                    tpos[0], tpos[1] = 3, 0
                elif tpos[1] == 20:
                    tpos[0], tpos[1] = 1, 7
            elif tpos[0] == 2:
                if tpos[1] >= len(score[2]):
                    tpos[0], tpos[1] = 1, tpos[1] + 1
            elif tpos[0] == 3:
                if tpos[1] >= len(score[3]):
                    tpos[0] = 1

            if tpos[1] < len(score[tpos[0]]):
                check = False
                for j in range(4):
                    if i == j:
                        continue
                    if tpos[1] >= 0 and tpos[0] == tt[j][0] and tpos[1] == tt[j][1]:
                        check = True
                        break
                if check:
                    continue
                ttotal += score[tpos[0]][tpos[1]]
            else:
                tpos[1] = -2
            dfs(k + 1, tt, ttotal)


dfs(0, [[0, 0] for _ in range(4)], 0)
print(answer)