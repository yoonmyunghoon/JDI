import sys
sys.stdin = open("14891_톱니바퀴.txt")

cogWheels = [list(map(int, input())) for _ in range(4)]
N = int(input())
info = []
for i in range(N):
    n, d = map(int, input().split())
    info.append([n, d])

check = [0, 0, 0, 0]

def rotation(n, d, before):
    if n == 1:
        if cogWheels[0][2] != cogWheels[1][-2] and before != 2:
            check[1] = d*(-1)
            rotation(2, d*(-1), n)
    elif n == 2:
        if cogWheels[0][2] != cogWheels[1][-2] and before != 1:
            check[0] = d*(-1)
            rotation(1, d*(-1), n)
        if cogWheels[1][2] != cogWheels[2][-2] and before != 3:
            check[2] = d*(-1)
            rotation(3, d*(-1), n)
    elif n == 3:
        if cogWheels[1][2] != cogWheels[2][-2] and before != 2:
            check[1] = d*(-1)
            rotation(2, d*(-1), n)
        if cogWheels[2][2] != cogWheels[3][-2] and before != 4:
            check[3] = d*(-1)
            rotation(4, d*(-1), n)
    else:
        if cogWheels[2][2] != cogWheels[3][-2] and before != 3:
            check[2] = d*(-1)
            rotation(3, d*(-1), n)

for i in range(N):
    check = [0, 0, 0, 0]
    check[info[i][0]-1] = info[i][1]
    rotation(info[i][0], info[i][1], 0)
    for j in range(len(check)):
        if check[j] == 1:
             a = cogWheels[j].pop()
             cogWheels[j].insert(0, a)
        elif check[j] == -1:
            a = cogWheels[j].pop(0)
            cogWheels[j].append(a)

result = cogWheels[0][0]*1+cogWheels[1][0]*2+cogWheels[2][0]*4+cogWheels[3][0]*8
print(result)


