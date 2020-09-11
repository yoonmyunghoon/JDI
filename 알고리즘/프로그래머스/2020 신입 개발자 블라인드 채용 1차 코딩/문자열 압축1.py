
def check(s, k):
    char = s[0:k]
    cnt = 0
    length = 0
    for i in range(0, len(s), k):
        if i+k >= len(s):
            if s[i:i + k] == char:
                cnt += 1
                length += len(str(cnt)) + k
            else:
                if cnt == 1:
                    length += k
                else:
                    length += len(str(cnt)) + k
                length += len(s) - i
        else:
            if s[i:i+k] == char:
                cnt += 1
            else:
                if cnt == 1:
                    length += k
                else:
                    length += len(str(cnt)) + k
                cnt = 1
                char = s[i:i+k]
    return length


def solution(s):
    limit = len(s)//2
    minimum = len(s)
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
