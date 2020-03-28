import sys
sys.stdin = open("input.txt")

def isWall(x, y):
    if 0 > x or x > 4: return True
    elif 0 > y or y > 4: return True
    else: return False

def calabs(a, b):
    if a-b > 0:
        return a-b
    else:
        return b-a

data = [list(map(int, input().split())) for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
sum = 0
for i in range(5):
    for j in range(5):
        for k in range(4):
            newX = i + dx[k]
            newY = j + dy[k]
            if isWall(newX, newY) == False:
                sum += calabs(data[newX][newY], data[i][j])
print(sum)


# def isWall(x, y):
#     if x < 0 or x >= 5 : return True
#     if y < 0 or y >= 5 : return True
#     return False
#
# def calAbs(x, y):
#     if x > y: return x-y
#     else: return y-x
#
#
# arr = [[0 for _ in range(5)] for _ in range(5)]
# for i in range(5):
#     arr[i] = list(map(int, input().split()))
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# sum = 0
#
# for x in range(len(arr)):
#     for y in range(len(arr[x])):
#         for i in range(4):
#             newX = x + dx[i]
#             newY = y + dy[i]
#             if isWall(newX, newY) == False:
#                 sum += calAbs(arr[x][y], arr[newX][newY])
# print("sum = {}".format(sum))


