import sys, copy
sys.stdin = open("12100_2046(Easy).txt")

# 0:상, 1:우, 2:하, 3:좌
arr = [0, 1, 2, 3]
q = 5
T = [0]*q


# 중복순열
def perm(n, r):
    global maximum
    if r == 0:
        max_in_blocks = move(T)
        if max_in_blocks > maximum:
            maximum = max_in_blocks
        return
    else:
        for i in range(n-1, -1, -1):
            arr[i], arr[n-1] = arr[n-1], arr[i]
            T[r-1] = arr[n-1]
            perm(n, r-1)
            arr[i], arr[n-1] = arr[n-1], arr[i]


# block 이동
def move(T):
    blocks = copy.deepcopy(blocks_og)
    for i in range(len(T)):
        if T[i] == 0:
            for y in range(N):
                # 밀기
                cnt = 0
                stores = []
                for k in range(N):
                    if blocks[k][y] != 0:
                        cnt += 1
                        stores.append(blocks[k][y])
                for l in range(N):
                    if l < cnt:
                        blocks[l][y] = stores[l]
                    else:
                        blocks[l][y] = 0
                # 합치기
                x = 1
                while x < N:
                    if blocks[x][y] == blocks[x-1][y]:
                        blocks[x-1][y] *= 2
                        blocks[x][y] = 0
                        x += 1
                    x += 1
                # 밀기
                cnt = 0
                stores = []
                for k in range(N):
                    if blocks[k][y] != 0:
                        cnt += 1
                        stores.append(blocks[k][y])
                for l in range(N):
                    if l < cnt:
                        blocks[l][y] = stores[l]
                    else:
                        blocks[l][y] = 0
        elif T[i] == 1:
            for x in range(N):
                cnt = 0
                stores = []
                for k in range(N - 1, -1, -1):
                    if blocks[x][k] != 0:
                        cnt += 1
                        stores.append(blocks[x][k])
                for l in range(N):
                    if l < cnt:
                        blocks[x][N - 1 - l] = stores[l]
                    else:
                        blocks[x][N - 1 - l] = 0

                y = N-2
                while y > -1:
                    if blocks[x][y] == blocks[x][y+1]:
                        blocks[x][y+1] *= 2
                        blocks[x][y] = 0
                        y -= 1
                    y -= 1

                cnt = 0
                stores = []
                for k in range(N - 1, -1, -1):
                    if blocks[x][k] != 0:
                        cnt += 1
                        stores.append(blocks[x][k])
                for l in range(N):
                    if l < cnt:
                        blocks[x][N - 1 - l] = stores[l]
                    else:
                        blocks[x][N - 1 - l] = 0
        elif T[i] == 2:
            for y in range(N):
                cnt = 0
                stores = []
                for k in range(N-1, -1, -1):
                    if blocks[k][y] != 0:
                        cnt += 1
                        stores.append(blocks[k][y])
                for l in range(N):
                    if l < cnt:
                        blocks[N-1-l][y] = stores[l]
                    else:
                        blocks[N-1-l][y] = 0

                x = N-2
                while x > -1:
                    if blocks[x][y] == blocks[x+1][y]:
                        blocks[x+1][y] *= 2
                        blocks[x][y] = 0
                        x -= 1
                    x -= 1

                cnt = 0
                stores = []
                for k in range(N - 1, -1, -1):
                    if blocks[k][y] != 0:
                        cnt += 1
                        stores.append(blocks[k][y])
                for l in range(N):
                    if l < cnt:
                        blocks[N - 1 - l][y] = stores[l]
                    else:
                        blocks[N - 1 - l][y] = 0
        else:
            for x in range(N):
                cnt = 0
                stores = []
                for k in range(N):
                    if blocks[x][k] != 0:
                        cnt += 1
                        stores.append(blocks[x][k])
                for l in range(N):
                    if l < cnt:
                        blocks[x][l] = stores[l]
                    else:
                        blocks[x][l] = 0

                y = 1
                while y < N:
                    if blocks[x][y] == blocks[x][y-1]:
                        blocks[x][y-1] *= 2
                        blocks[x][y] = 0
                        y += 1
                    y += 1

                cnt = 0
                stores = []
                for k in range(N):
                    if blocks[x][k] != 0:
                        cnt += 1
                        stores.append(blocks[x][k])
                for l in range(N):
                    if l < cnt:
                        blocks[x][l] = stores[l]
                    else:
                        blocks[x][l] = 0

    max_in_blocks = 0
    for i in range(N):
        for j in range(N):
            if blocks[i][j] > max_in_blocks:
                max_in_blocks = blocks[i][j]
    return max_in_blocks


N = int(input())
blocks_og = [list(map(int, input().split())) for _ in range(N)]

maximum = 0
perm(4, q)
print(maximum)


