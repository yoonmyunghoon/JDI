N = 7
PI = list(range(N+1))
print(PI)
data = [(2, 3), (4, 5), (4, 6), (7, 4)]

def find_set(x):
    if PI[x] == x:
        return x
    else:
        PI[x] = find_set(PI[x])
        return PI[x]

def union(x, y):
    a = find_set(x)
    b = find_set(y)
    PI[b] = a

for i, j in data:
    if find_set(i) != find_set(j):
        union(i, j)

print(PI)

