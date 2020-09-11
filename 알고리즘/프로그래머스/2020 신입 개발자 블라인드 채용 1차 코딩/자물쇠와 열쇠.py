
def rotate(key):
    L = len(key)
    new_key = [[0 for _ in range(L)] for _ in range(L)]
    for i in range(L):
        for j in range(L):
            new_key[j][L-i-1] = key[i][j]
    return new_key


def check(cube, key, m, l, hole):
    for i in range(l-m):
        for j in range(l-m):
            flag = 0
            hole_check = 0
            for x in range(m):
                if flag == 1:
                    break
                for y in range(m):
                    if flag == 1:
                        break
                    if cube[i+x][j+y] + key[x][y] == 2:
                        flag = 1
                        break
                    if [i+x, j+y] in hole:
                        if key[x][y] == 1:
                            hole_check += 1
            if flag == 1:
                continue
            else:
                if hole_check == len(hole):
                    return True
                continue
    return False


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
    flag = 0
    key1 = key
    if check(cube, key1, M, L, hole_position):
        flag = 1
    if flag:
        return True
    key2 = rotate(key1)
    if check(cube, key2, M, L, hole_position):
        flag = 1
    if flag:
        return True
    key3 = rotate(key2)
    if check(cube, key3, M, L, hole_position):
        flag = 1
    if flag:
        return True
    key4 = rotate(key3)
    if check(cube, key4, M, L, hole_position):
        flag = 1
    if flag:
        return True
    return False


KEY = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
LOCK = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(KEY, LOCK))