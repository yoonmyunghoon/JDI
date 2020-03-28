import sys
sys.stdin = open("2309_일곱난쟁이.txt")

hap = 0
nanjangs = []
for i in range(9):
    a = int(input())
    nanjangs.append(a)
    hap += a
hap -= 100
c1, c2 = -1, -1
for i in range(8):
    for j in range(i+1, 9):
        if nanjangs[i] + nanjangs[j] == hap:
            c1, c2 = i, j
r_nanjangs = []
for i in range(9):
    if i != c1 and i != c2:
        r_nanjangs.append(nanjangs[i])
r_nanjangs.sort()
for i in range(7):
    print(r_nanjangs[i])

