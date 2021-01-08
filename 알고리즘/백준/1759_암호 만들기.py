import sys
sys.stdin = open("1759_암호 만들기.txt")


def find_key(n, r, cnt_mo, cnt_ja):
    if r == L:
        if cnt_mo >= 1 and cnt_ja >= 2:
            print(''.join(result))
        return
    elif L-r > C-n:
        return
    else:
        result[r] = data[n]
        if data[n] in 'aeiou':
            find_key(n + 1, r + 1, cnt_mo + 1, cnt_ja)
        else:
            find_key(n + 1, r + 1, cnt_mo, cnt_ja + 1)
        find_key(n+1, r, cnt_mo, cnt_ja)


L, C = map(int, input().split())
data = list(input().split())
data.sort()
result = ['A']*L
find_key(0, 0, 0, 0)