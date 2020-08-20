import sys
sys.stdin = open("2641_다각형그리기.txt")


def comparison(S1, S2):
    m = 0
    S2 = S2 * 2
    while m < N:
        if S1 == S2[m:m+N]:
            return 1
        else:
            m += 1
    return 0


N = int(input())
drawing = list(map(int, input().split()))
s_drawing = []
for i in range(len(drawing)):
    if drawing[i] == 1: s_drawing.append(3)
    elif drawing[i] == 2: s_drawing.append(4)
    elif drawing[i] == 3: s_drawing.append(1)
    elif drawing[i] == 4: s_drawing.append(2)

s_drawing.reverse()
result = []
cnt = 0
M = int(input())
for i in range(M):
    data = list(map(int, input().split()))
    if comparison(drawing, data):
        result.append(data)
        cnt += 1
    else:
        if comparison(s_drawing, data):
            result.append(data)
            cnt += 1
print(cnt)
for i in range(len(result)):
    for j in range(N):
        print(result[i][j], end=' ')
    print()