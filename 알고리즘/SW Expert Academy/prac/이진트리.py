V = 13
data = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]


def preorder(x):
    if x:
        print(x, end=" ")
        preorder(G[x][0])
        preorder(G[x][1])


G = [[0]*3 for _ in range(V+1)]
for i in range(len(data)//2):
    p = data[i*2]
    c = data[i*2+1]
    if G[p][0] == 0:
        G[p][0] = c
    else:
        G[p][1] = c
    G[c][2] = p
for i in G:
    print(i)
preorder(1)

