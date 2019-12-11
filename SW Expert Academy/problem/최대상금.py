import sys, time
sys.stdin = open("최대상금.txt")
starttime = time.time()

def perm(n, c):
    global C, result
    if c == C:
        result.add(''.join(arr))
    else:
        for i in range(n-1):
            for j in range(i+1, n):
                arr[i], arr[j] = arr[j], arr[i]
                perm(n, c+1)
                arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for tc in range(1, T+1):
    N, C = map(int, input().split())
    arr = list(str(N))
    result = set()
    if C > 5:
        if C % 2:
            C = 5
        else:
            C = 4
    perm(len(arr), 0)
    # print(result)
    # print(N, C, arr)
    result = list(map(int, result))
    print(max(result))

print(time.time() - starttime)