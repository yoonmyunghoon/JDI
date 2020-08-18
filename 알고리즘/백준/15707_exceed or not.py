import sys
sys.stdin = open("15707_exceed or not.txt")

a, b, r = map(int, input().split())
print(a, b, r)
if a * b > r:
    print('overflow')
else:
    print(a * b)