import sys
sys.stdin = open("17825_주사위 윷놀이.txt")

def dfs(n, maxmal, hap):
    global types, roads, mals
    if maxmal >= 4:
        return
    if n == len(turns):
        print(mals, hap)
        return
    for i in range(4):
        if maxmal < i:
            break
        elif maxmal == i:
            mals[i] += turns[n]
            if mals[i] == 5 and roads[types[i]][4] == 10:
                types[i] = 5
            elif mals[i] == 10 and roads[types[i]][9] == 20:
                types[i] = 10
            elif mals[i] == 15 and roads[types[i]][14] == 30:
                types[i] = 15
            dfs(n + 1, maxmal + 1, hap + roads[types[i]][mals[i]-1])
            mals[i] -= turns[n]
        else:
            mals[i] += turns[n]
            if mals[i] == 5 and roads[types[i]][4] == 10:
                types[i] = 5
            elif mals[i] == 10 and roads[types[i]][9] == 20:
                types[i] = 10
            elif mals[i] == 15 and roads[types[i]][14] == 30:
                types[i] = 15
            dfs(n + 1, maxmal, hap + roads[types[i]][mals[i]-1])
            mals[i] -= turns[n]
roads = {
    0: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
    5: [2, 4, 6, 8, 10, 13, 16, 19, 25, 30, 35, 40],
    10: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30, 35, 40],
    15: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 27, 26, 25, 30, 35, 40]
}
turns = list(map(int, input().split()))
mals = [0, 0, 0, 0]
types = [0, 0, 0, 0]
print(turns)
dfs(0, 0, 0)

