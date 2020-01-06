import sys
sys.stdin = open("2628_종이자르기.txt")

col, row = map(int, input().split())
n = int(input())
rows = []
cols = []
for i in range(n):
    info, num = map(int, input().split())
    if info == 0:
        rows.append(num)
    else:
        cols.append(num)
rows.sort()
rows.append(row)
cols.sort()
cols.append(col)
maxrow = rows[0]
maxcol = cols[0]
for i in range(1, len(rows)):
    d = rows[i] - rows[i-1]
    if maxrow < d:
        maxrow = d
for i in range(1, len(cols)):
    d = cols[i] - cols[i-1]
    if maxcol < d:
        maxcol = d

print(maxrow*maxcol)