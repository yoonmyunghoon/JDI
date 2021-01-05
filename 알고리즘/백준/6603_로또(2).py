import sys
sys.stdin = open("6603_로또.txt")


def dfs(start, depth):
    if depth == 6:
        print(' '.join(map(str, line)))
    else:
        for i in range(start, k):
            line[depth] = S[i]
            dfs(i + 1, depth + 1)


while 1:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    k = data[0]
    S = data[1:]
    line = [0]*6
    dfs(0, 0)
    print()
