
def check(arr):
    arr.append("")
    hl = 0
    cnt = 1
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            cnt += 1
        else:
            if cnt > 1:
                hl += len(str(cnt))
            hl += len(arr[i])
            cnt = 1
    return hl


def solution(s):
    minimum = len(s)
    for i in range(1, int(len(s)/2)+1):
        arr = []
        for j in range(0, len(s), i):
            arr.append(s[j:j+i])
        result = check(arr)
        if minimum > result:
            minimum = result
    return minimum

ss = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
    'aaaaaa',
]
for s in ss:
    print(solution(s))
