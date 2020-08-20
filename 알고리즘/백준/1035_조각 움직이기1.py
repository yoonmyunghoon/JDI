import sys
sys.stdin = open("1035_조각 움직이기.txt")


# 순열 / 최소 거리를 구하기
def perm(n, k):
    global minimum
    if n == k:
        distance = 0
        for a in range(N):
            distance += (diff(position[a][0], info[T[arr[a]]][0]) + diff(position[a][1], info[T[arr[a]]][1]))
        if minimum > distance:
            minimum = distance
        return
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]


# 조합 / 조건을 충족하도록 이동된 조각들의 위치 구하기
def comb(n, r):
    if r == 0:
        for i in range(N):
            if not (min_x <= info[T[i]][0] <= max_x and min_y <= info[T[i]][1] <= max_y):
                return
        if check():
            perm(N, 0)
    elif n < r:
        return
    else:
        T[r-1] = A[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


# Union-Find / 조각들이 연결되어있는지 확인하기 위한 용도
def find(n):
    global p
    if p[n] < 0:
        return n
    else:
        p[n] = find(p[n])
        return p[n]


def union(a, b):
    global p
    a = find(a)
    b = find(b)
    if a == b:
        return
    else:
        p[b] = a

# 각 조각들의 거리를 구해서 조건을 만족하면 연결시킴
def check():
    global p
    p = [-1]*N
    for i in range(N-1):
        for j in range(i+1, N):
            if diff(info[T[i]][0], info[T[j]][0]) + diff(info[T[i]][1], info[T[j]][1]) == 1:
                union(i, j)
    if p.count(-1) == 1:
        c_set = set()
        for k in range(N):
            c_set.add(find(k))
            if len(c_set) == 1:
                return 1
            else:
                return 0
    else:
        return 0

# 절댓값구하기 / 거리 구할 때 사용
def diff(a, b):
    if a > b:
        return a - b
    else:
        return b - a


board = [list(input()) for _ in range(5)]
position = []
info = []
# 조각들이 이동할 수 있는 최대 범위를 표시해주기 위한 변수들, 이 범위를 벗어나는 이동에 대해서는 따져볼 필요가 없음
max_x = 0
min_x = 4
max_y = 0
min_y = 4
for i in range(5):
    for j in range(5):
        info.append([i, j])
        if board[i][j] == '*':
            position.append([i, j])
            if max_x < i:
                max_x = i
            if min_x > i:
                min_x = i
            if max_y < j:
                max_y = j
            if min_y > j:
                min_y = j
N = len(position)

# 조각이 하나인 경우 0 출력
if N == 1:
    print(0)
else:
    p = [-1]*N
    minimum = 987654321
    arr = list(range(N))
    T = [0] * N
    A = list(range(25))
    comb(25, N)
    print(minimum)