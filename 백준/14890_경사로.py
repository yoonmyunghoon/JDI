import sys
sys.stdin = open("14890_경사로.txt")

N, L = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
for i in map:
    print(i)
print()

count = 0
smaller = 0
for i in range(N):
    tmp = 1
    for j in range(N-1):
        if map[i][j] == map[i][j+1]:
            tmp += 1
        elif map[i][j] + 1 == map[i][j+1]:
            if smaller == 1:
                if tmp < L:
                    break
                else:
                    tmp -= L
                    if tmp < L:
                        break
                    else:
                        tmp = 1
                        smaller = 0
            if tmp < L:
                break
        elif map[i][j] == map[i][j+1] + 1:
            if smaller == 1:
                if tmp < L:
                    break
            smaller = 1
            tmp = 1
        else:
            break
        if j == N-1:
            if map[i][j] == map[i][j+1]:
                count += 1
            elif map[i][j] + 1 == map[i][j+1]:
                if tmp < L:
                    break
                else:
                    count += 1
            elif map[i][j] == map[i][j+1] + 1:
                if L > 1:
                    break
                else:
                    count += 1
            else:
                break

print(count)
