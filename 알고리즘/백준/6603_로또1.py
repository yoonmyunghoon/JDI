import sys
sys.stdin = open("6603_로또.txt")


def dfs(start, depth):
    if depth == 6:
        print(' '.join(map(str, comb)))
        return
    for i in range(start, len(a)):
        comb[depth] = a[i]
        dfs(i + 1, depth + 1)


while True:
    l = list(map(int, input().split()))
    n = l[0]
    if n == 0:
        break
    a = l[1:]
    comb = [0] * 6
    dfs(0, 0)
    print()