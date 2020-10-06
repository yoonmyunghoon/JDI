import sys
sys.stdin = open("1484_다이어트.txt")

G = int(input())
data = [i*i for i in range(1, int(G/2+0.5)+1)]
result = []
start = 0
end = 0
diff = 0
while 1:
    if end == len(data) - 1:
        if diff < G:
            break
    if start == len(data) - 1 and end == len(data) - 1:
        break
    else:
        if diff < G:
            end += 1
            diff = diff + (data[end] - data[end-1])
        elif diff == G:
            result.append(end+1)
            start += 1
            diff = diff - (data[start] - data[start-1])
        else:
            start += 1
            diff = diff - (data[start] - data[start - 1])
if len(result):
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)
