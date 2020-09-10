
def check(s, k):
    char = s[0:k]
    start = k
    cnt = 1
    length = 0
    while 1:
        if start+k > len(s):
            if cnt == 1:
                length += k
            else:
                length += (k + len(str(cnt)))
            length += (len(s) - start)
            break
        if s[start:start+k] == char:
            cnt += 1
        else:
            if cnt == 1:
                length += k
            else:
                length += k + len(str(cnt))
            char = s[start:start+k]
            cnt = 1
        start += k
    return length


def solution(s):
    limit = len(s)//2
    minimum = 1000
    for i in range(1, limit+1):
        res = check(s, i)
        if minimum > res:
            minimum = res
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
