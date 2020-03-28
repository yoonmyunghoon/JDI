import sys
sys.stdin = open("input.txt")

def isWall(x, y):
    if x < 0 or x >= N: return True
    elif y < 0 or y >= N: return True
    elif pipe[x][y] == 0: return True
    else: return False

def move(before, now, count):
    global Min
    if Min <= count:
        return
    if isWall(now[0], now[1]):
        return
    if now[0] == N-1 and now[1] == N-1:
        Min = count
        data.append(count)
        return
    x = now[0]
    y = now[1]
    if pipe[x][y] == 1:
        if isWall(x, y-1) == False and before != [x, y-1]:
            if pipe[x][y-1] == 1 or pipe[x][y-1] == 2:
                pipe[x][y - 1] = 1
                move([x, y], [x, y - 1], count + 1)
            else:
                for i in range(2):
                    if i == 0:
                        a = pipe[x][y - 1]
                        pipe[x][y - 1] = 3
                        move([x, y], [x, y - 1], count + 1)
                        pipe[x][y - 1] = a
                    else:
                        a = pipe[x][y - 1]
                        pipe[x][y - 1] = 6
                        move([x, y], [x, y - 1], count + 1)
                        pipe[x][y - 1] = a
        if isWall(x, y + 1) == False and before != [x, y+1]:
            if pipe[x][y + 1] == 1 or pipe[x][y + 1] == 2:
                pipe[x][y + 1] = 1
                move([x, y], [x, y + 1], count + 1)
            else:
                for i in range(2):
                    if i == 0:
                        a = pipe[x][y + 1]
                        pipe[x][y + 1] = 4
                        move([x, y], [x, y + 1], count + 1)
                        pipe[x][y + 1] = a
                    else:
                        a= pipe[x][y + 1]
                        pipe[x][y + 1] = 5
                        move([x, y], [x, y + 1], count + 1)
                        pipe[x][y + 1] = a
    if pipe[x][y] == 2:
        if isWall(x-1, y) == False and before != [x-1, y]:
            if pipe[x-1][y] == 1 or pipe[x-1][y] == 2:
                pipe[x - 1][y] = 2
                move([x, y], [x-1, y], count + 1)
            else:
                for i in range(2):
                    if i == 0:
                        a= pipe[x-1][y]
                        pipe[x-1][y] = 3
                        move([x, y], [x - 1, y], count + 1)
                        pipe[x - 1][y] =a
                    else:
                        a= pipe[x-1][y]
                        pipe[x-1][y] = 4
                        move([x, y], [x-1, y], count + 1)
                        pipe[x - 1][y]=a
        if isWall(x+1, y) == False and before != [x+1, y]:
            if pipe[x + 1][y] == 1 or pipe[x + 1][y] == 2:
                pipe[x + 1][y] = 2
                move([x, y], [x+1, y], count + 1)
            else:
                for i in range(2):
                    if i == 0:
                        a= pipe[x + 1][y]
                        pipe[x + 1][y] = 5
                        move([x, y], [x+1, y], count + 1)
                        pipe[x + 1][y]=a
                    else:
                        a=pipe[x + 1][y]
                        pipe[x + 1][y] = 6
                        move([x, y], [x+1, y], count + 1)
                        pipe[x + 1][y]=a
    if pipe[x][y] == 3:
        if isWall(x + 1, y) == False and before != [x + 1, y]:
            if pipe[x + 1][y] == 1 or pipe[x + 1][y] == 2:
                pipe[x + 1][y] = 2
                move([x, y], [x + 1, y], count + 1)
            else:
                for i in range(2):
                    if i == 0:
                        a=pipe[x + 1][y]
                        pipe[x + 1][y] = 5
                        move([x, y], [x + 1, y], count + 1)
                        pipe[x + 1][y]=a
                    else:
                        a=pipe[x + 1][y]
                        pipe[x + 1][y] = 6
                        move([x, y], [x + 1, y], count + 1)
                        pipe[x + 1][y]=a
        if isWall(x, y + 1) == False and before != [x, y + 1]:
            if pipe[x][y + 1] == 1 or pipe[x][y + 1] == 2:
                pipe[x][y + 1] = 1
                move([x, y], [x, y + 1], count + 1)
            else:
                for i in range(2):
                    if i == 0:
                        a=pipe[x][y + 1]
                        pipe[x][y + 1] = 4
                        move([x, y], [x, y + 1], count + 1)
                        pipe[x][y + 1]=a
                    else:
                        a=pipe[x][y + 1]
                        pipe[x][y + 1] = 5
                        move([x, y], [x, y + 1], count + 1)
                        pipe[x][y + 1]=a
    if pipe[x][y] == 4:
        if isWall(x, y - 1) == False and before != [x, y - 1]:
            if pipe[x][y - 1] == 1 or pipe[x][y - 1] == 2:
                pipe[x][y - 1] = 1
                move([x, y], [x, y - 1], count + 1)
            else:
                for i in range(2):
                    if i == 0:
                        a=pipe[x][y - 1]
                        pipe[x][y - 1] = 3
                        move([x, y], [x, y - 1], count + 1)
                        pipe[x][y - 1]=a
                    else:
                        a=pipe[x][y - 1]
                        pipe[x][y - 1] = 6
                        move([x, y], [x, y - 1], count + 1)
                        pipe[x][y - 1]=a
        if isWall(x + 1, y) == False and before != [x + 1, y]:
            if pipe[x + 1][y] == 1 or pipe[x + 1][y] == 2:
                pipe[x + 1][y] = 2
                move([x, y], [x + 1, y], count + 1)
            else:
                for i in range(2):
                    if i == 0:
                        a=pipe[x + 1][y]
                        pipe[x + 1][y] = 5
                        move([x, y], [x + 1, y], count + 1)
                        pipe[x + 1][y]=a
                    else:
                        a=pipe[x + 1][y]
                        pipe[x + 1][y] = 6
                        move([x, y], [x + 1, y], count + 1)
                        pipe[x + 1][y]=a
    if pipe[x][y] == 5:
        if isWall(x, y - 1) == False and before != [x, y - 1]:
            if pipe[x][y - 1] == 1 or pipe[x][y - 1] == 2:
                pipe[x][y - 1] = 1
                move([x, y], [x, y - 1], count + 1)
            else:
                for i in range(2):
                    if i == 0:
                        a=pipe[x][y - 1]
                        pipe[x][y - 1] = 3
                        move([x, y], [x, y - 1], count + 1)
                        pipe[x][y - 1]=a
                    else:
                        a=pipe[x][y - 1]
                        pipe[x][y - 1] = 6
                        move([x, y], [x, y - 1], count + 1)
                        pipe[x][y - 1]=a
        if isWall(x - 1, y) == False and before != [x - 1, y]:
            if pipe[x - 1][y] == 1 or pipe[x - 1][y] == 2:
                pipe[x - 1][y] = 2
                move([x, y], [x - 1, y], count + 1)
            else:
                for i in range(2):
                    if i == 0:
                        a=pipe[x - 1][y]
                        pipe[x - 1][y] = 3
                        move([x, y], [x - 1, y], count + 1)
                        pipe[x - 1][y]=a
                    else:
                        a=pipe[x - 1][y]
                        pipe[x - 1][y] = 4
                        move([x, y], [x - 1, y], count + 1)
                        pipe[x - 1][y]=a
    if pipe[x][y] == 6:
        if isWall(x, y + 1) == False and before != [x, y + 1]:
            if pipe[x][y + 1] == 1 or pipe[x][y + 1] == 2:
                pipe[x][y + 1] = 1
                move([x, y], [x, y + 1], count + 1)
            else:
                for i in range(2):
                    if i == 0:
                        a=pipe[x][y + 1]
                        pipe[x][y + 1] = 4
                        move([x, y], [x, y + 1], count + 1)
                        pipe[x][y + 1]=a
                    else:
                        a=pipe[x][y + 1]
                        pipe[x][y + 1] = 5
                        move([x, y], [x, y + 1], count + 1)
                        pipe[x][y + 1]=a
        if isWall(x - 1, y) == False and before != [x - 1, y]:
            if pipe[x - 1][y] == 1 or pipe[x - 1][y] == 2:
                pipe[x - 1][y] = 2
                move([x, y], [x - 1, y], count + 1)
            else:
                for i in range(2):
                    if i == 0:
                        a=pipe[x - 1][y]
                        pipe[x - 1][y] = 3
                        move([x, y], [x - 1, y], count + 1)
                        pipe[x - 1][y]=a
                    else:
                        a=pipe[x - 1][y]
                        pipe[x - 1][y] = 4
                        move([x, y], [x - 1, y], count + 1)
                        pipe[x - 1][y]=a


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pipe = [list(map(int, input().split())) for _ in range(N)]
    data = []
    Min = N*N
    move([0, -1], [0, 0], 1)
    print(data)
    print()
    for i in pipe:
        print(i)
    print()
    print()

