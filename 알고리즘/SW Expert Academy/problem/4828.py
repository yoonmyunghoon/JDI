t = int(input())
lis = []

def dif_min_max(n, l):
    a = sorted(l)
    lis.append(a[n-1] - a[0])

for i in range(t):
    n = int(input())
    l = list(map(int, input().split(' ')))
    dif_min_max(n, l)

for i in range(len(lis)):
    print('#{} {}'.format(i+1, lis[i]))


