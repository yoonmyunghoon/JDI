import sys
sys.stdin = open("3109_빵집.txt")

R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]
for i in Map:
    print(i)