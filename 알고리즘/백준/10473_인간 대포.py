import sys
sys.stdin = open("10473_인간 대포.txt")
# input = sys.stdin.readline

X, Y = map(float, input().split())
Px, Py = map(float, input().split())
num = int(input())
positions = []
for i in range(num):
    A, B = map(float, input().split())
    positions.append([A, B])
print(positions)