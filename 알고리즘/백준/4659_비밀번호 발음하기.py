import sys
sys.stdin = open("4659_비밀번호 발음하기.txt")


def check(s):
    global result
    flag = 0
    for c in s:
        if c in 'aeiou':
            flag = 1
            break
    if flag != 1:
        result = 0
        return

    jaum = 0
    moum = 0
    for c in s:
        if c in 'aeiou':
            jaum = 0
            moum += 1
            if moum >= 3:
                result = 0
                return
        else:
            moum = 0
            jaum += 1
            if jaum >= 3:
                result = 0
                return

    bc = ''
    for c in s:
        if bc == c:
            if c == 'o' or c == 'e':
                bc = c
            else:
                result = 0
                return
        else:
            bc = c


while 1:
    result = 1
    word = input()
    if word == 'end':
        break
    else:
        check(word)
        if result == 1:
            print('<{}> is acceptable.'.format(word))
        elif result == 0:
            print('<{}> is not acceptable.'.format(word))