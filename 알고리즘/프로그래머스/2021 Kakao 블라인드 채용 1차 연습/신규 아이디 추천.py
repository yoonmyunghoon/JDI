def solution(new_id):
    # 1
    answer = new_id.lower()
    # 2
    excep = '~!@#$%^&*()=+[{]}:?,<>/'
    for e in excep:
        answer = answer.replace(e, '')
    # 3
    while 1:
        if answer.find('..') == -1:
            break
        else:
            answer = answer.replace('..', '.')
    # 4, 5
    if answer[0] == '.':
        answer = answer[1:]
        if answer == '':
            answer = 'a'
    if answer[-1] == '.':
        answer = answer[:-1]
        if answer == '':
            answer = 'a'
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:14]
    # 7
    if len(answer) <= 2:
        answer += answer[-1] * (3-len(answer))

    return answer


N = "abcdefghijklmn.p"
print(solution(N))
