
def rotate(key):
    L = len(key)
    new_key = [[0 for _ in range(L)] for _ in range(L)]
    for i in range(L):
        for j in range(L):
            new_key[j][L-i-1] = key[i][j]
    return new_key


def check(cube, k, m, l, hole):
    for i in range(l-m+1):
        for j in range(l-m+1):
            hole_cnt = 0
            for x in range(m):
                for y in range(m):
                    if cube[i+x][j+y] == 0 and ([i+x, j+y] in hole):
                        hole_cnt += 1
            if hole_cnt != len(hole):
                continue
            else:
                flag = 0
                hole_check = 0
                for x in range(m):
                    for y in range(m):
                        if cube[i+x][j+y] + k[x][y] == 2:
                            flag = 1
                            break
                        if [i+x, j+y] in hole:
                            if k[x][y] == 1:
                                hole_check += 1
                    if flag == 1:
                        break
                if flag == 1:
                    continue
                else:
                    if hole_check == len(hole):
                        return 1
                    continue
    return 0


def solution(key, lock):
    M = len(key)
    N = len(lock)
    L = N + 2*(M-1)
    hole_position = []
    lx = M-1
    ly = M-1
    cube = [[0 for _ in range(L)] for _ in range(L)]
    for i in range(lx, lx+N):
        for j in range(ly, ly+N):
            cube[i][j] = lock[i-lx][j-ly]
            if cube[i][j] == 0:
                hole_position.append([i, j])
    key1 = key
    key2 = rotate(key1)
    key3 = rotate(key2)
    key4 = rotate(key3)
    keys = [key1, key2, key3, key4]
    for k_ in keys:
        if check(cube, k_, M, L, hole_position):
            return True
    return False


KEY = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
LOCK = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(KEY, LOCK))