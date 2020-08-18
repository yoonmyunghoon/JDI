import sys
sys.stdin = open("14710_고장난 시계.txt")

m, s = map(int, input().split())
if (m % 30) * 12 == s:
    print('O')
else:
    print('X')