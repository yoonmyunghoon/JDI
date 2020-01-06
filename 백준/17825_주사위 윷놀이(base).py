import sys
sys.stdin = open("17825_주사위 윷놀이.txt")

# n: 몇번쨰, maxmal: 몇번쨰 말까지 사용할지(0, 1, 2, 3 이 올 수 있음), hap: 합
def dfs(n, maxmal):
    global maximum
    if maxmal > 3:
        return
    if n == len(turns):
        if maxmal == 3:
            print(mals, maxmal)
        return
    for i in range(4):
        if i == maxmal:
            if maxmal >= 3:
                continue
            mals[i] += turns[n]
            dfs(n + 1, maxmal + 1)
            mals[i] -= turns[n]
        else:
            mals[i] += turns[n]
            dfs(n + 1, maxmal)
            mals[i] -= turns[n]

turns = list(map(int, input().split()))
mals = [0, 0, 0, 0]
types = [0, 0, 0, 0]
visited = [0, 0, 0, 0]
dfs(0, 0)


