import sys
sys.stdin = open("14890_경사로.txt")

N, L = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]


count = 0
smaller = 0
for i in range(N):
    tmp = 1
    smaller = 0
    for j in range(N-1):
        if map[i][j] == map[i][j+1]:
            tmp += 1
        elif map[i][j] + 1 == map[i][j+1]:
            if smaller == 1:
                if tmp < 2*L:
                    break
                else:
                    tmp = 1
                    smaller = 0
            else:
                if tmp < L:
                    break
                else:
                    tmp = 1
        elif map[i][j] == map[i][j+1] + 1:
            if smaller == 1:
                if tmp < L:
                    break
            smaller = 1
            tmp = 1
        else:
            break
        if j == N-2:
            if map[i][j] == map[i][j+1]:
                if smaller == 1:
                    if tmp >= L:
                        count += 1
                    else:
                        break
                else:
                    count += 1
            elif map[i][j] + 1 == map[i][j+1]:
                count += 1
            elif map[i][j] == map[i][j+1] + 1:
                if L > 1:
                    break
                else:
                    count += 1
            else:
                break

for i in range(N):
    tmp = 1
    smaller = 0
    for j in range(N-1):
        if map[j][i] == map[j+1][i]:
            tmp += 1
        elif map[j][i] + 1 == map[j+1][i]:
            if smaller == 1:
                if tmp < 2*L:
                    break
                else:
                    tmp = 1
                    smaller = 0
            else:
                if tmp < L:
                    break
                else:
                    tmp = 1
        elif map[j][i] == map[j+1][i] + 1:
            if smaller == 1:
                if tmp < L:
                    break
            smaller = 1
            tmp = 1
        else:
            break
        if j == N-2:
            if map[j][i] == map[j+1][i]:
                if smaller == 1:
                    if tmp >= L:
                        count += 1
                    else:
                        break
                else:
                    count += 1
            elif map[j][i] + 1 == map[j+1][i]:
                count += 1
            elif map[j][i] == map[j+1][i] + 1:
                if L > 1:
                    break
                else:
                    count += 1
            else:
                break

print(count)
