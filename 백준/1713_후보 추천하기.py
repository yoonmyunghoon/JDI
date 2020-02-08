import sys
sys.stdin = open("1713_후보 추천하기.txt")

N = int(input())
pics = []
reco = int(input())
candidates = list(map(int, input().split()))

for i in range(reco):
    if len(pics) == 0:
        pics.append([candidates[i], 1, 0])
    elif len(pics) < N:
        for j in range(len(pics)):
            if pics[j][0] == candidates[i]:
                pics[j][1] += 1
                break
        else:
            pics.append([candidates[i], 1, 0])
    else:
        for j in range(len(pics)):
            if pics[j][0] == candidates[i]:
                pics[j][1] += 1
                break
        else:
            minimum = 1001
            positions = []
            for k in range(len(pics)):
                if pics[k][1] < minimum:
                    minimum = pics[k][1]
            for a in range(len(pics)):
                if pics[a][1] == minimum:
                    positions.append([pics[a][2], a])
            if len(positions) == 1:
                pics[positions[0][1]] = [candidates[i], 1, 0]
            else:
                positions.sort(reverse=True)
                pics[positions[0][1]] = [candidates[i], 1, 0]
    for c in range(len(pics)):
        pics[c][2] += 1

pick = []
for i in range(N):
    pick.append(pics[i][0])
pick.sort()
for i in range(N):
    print(pick[i], end=' ')
