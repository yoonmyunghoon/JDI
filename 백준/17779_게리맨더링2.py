import sys
sys.stdin = open("17779_게리맨더링2.txt")

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

def cal1(x, y, d1):
    hap = 0
    ce = y
    for r in range(x+d1):
        if r < x:
            for c in range(y+1):
                hap += A[r][c]
        else:
            ce -= 1
            for c in range(ce+1):
                hap += A[r][c]
    return hap

def cal2(x, y, d2):
    hap = 0
    cs = y
    for r in range(x+d2+1):
        if r < x:
            for c in range(y+1, N):
                hap += A[r][c]
        else:
            cs += 1
            for c in range(cs, N):
                hap += A[r][c]
    return hap

def cal3(x, y, d1, d2):
    hap = 0
    ce = y - d1
    for r in range(x+d1, N):
        if r > x+d1+d2:
            for c in range(y-d1+d2):
                hap += A[r][c]
        else:
            ce += 1
            for c in range(ce-1):
                hap += A[r][c]
    return hap

def cal4(x, y, d1, d2):
    hap = 0
    cs = y+d2
    for r in range(x + d2+1, N):
        if r > x + d1 + d2:
            for c in range(y - d1 + d2, N):
                hap += A[r][c]
        else:
            cs -= 1
            for c in range(cs+1, N):
                hap += A[r][c]
    return hap

def cal5(x, y, d1, d2):
    hap = 0
    cs, ce = y, y
    for r in range(x, x+d1+d2+1):
        if r-x <= d2:
            ce += 1
        else:
            ce -= 1
        if r-x <= d1:
            cs -= 1
        else:
            cs += 1
        for c in range(cs+1, ce):
            hap += A[r][c]
    return hap

mindiff = 987654321
for x in range(N-2):
    for y in range(1, N-1):
        for d1 in range(1, y+1):
            for d2 in range(1, N-y):
                if d1+d2 < N-x:
                    a1 = cal1(x, y, d1)
                    a2 = cal2(x, y, d2)
                    a3 = cal3(x, y, d1, d2)
                    a4 = cal4(x, y, d1, d2)
                    a5 = cal5(x, y, d1, d2)
                    maxa = max(a1, a2, a3, a4, a5)
                    mina = min(a1, a2, a3, a4, a5)
                    if mindiff > maxa-mina:
                        mindiff = maxa-mina

print(mindiff)






