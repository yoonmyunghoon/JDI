import sys
sys.stdin = open("2096_내려가기.txt")

N = int(input())
xa, xb, xc = map(int, input().split())
na, nb, nc = xa, xb, xc
for i in range(N-1):
    a, b, c = map(int, input().split())
    xa, xb, xc = max(xa, xb) + a, max(xa, xb, xc) + b, max(xb, xc) + c
    na, nb, nc = min(na, nb) + a, min(na, nb, nc) + b, min(nb, nc) + c
print(max(xa, xb, xc), min(na, nb, nc))


