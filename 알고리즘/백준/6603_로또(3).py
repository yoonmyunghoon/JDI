import sys
sys.stdin = open("6603_로또.txt")


def comb(n, r):
    if r == 0:
        for i in range(5, -1, -1):
            print(line[i], end=' ')
        print()
    elif n < r:
        return
    else:
        line[r-1] = S[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


while 1:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    k = data[0]
    S = data[1:]
    S.reverse()
    line = [0]*6
    comb(k, 6)
    print()
