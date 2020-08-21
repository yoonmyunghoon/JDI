import sys
sys.stdin = open("6603_로또.txt")


def comb(n, r):
    if r == 0:
        for i in range(5, -1, -1):
            print(T[i], end=' ')
        print()
    elif n < r:
        return
    else:
        T[r-1] = S[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


while 1:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break
    k = line[0]
    S = line[1:]
    S.reverse()
    T = [0] * 6
    comb(k, 6)
    print()