

def solution(new_id):
    new_id = new_id.lower()
    check = '~!@#$%^&*()=+[{]}:?,<>'
    for c in check:
        if c in new_id:
            new_id = new_id.replace(c, '')
    for n in range(len(new_id), 0, -1):
        if '.'*n in new_id:
            new_id = new_id.replace('.'*n, '.')
    if new_id == '':
        new_id = 'a'
    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id == '':
        new_id = 'a'
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    if new_id == '':
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) <= 2:
        temp = new_id[-1]
        while len(new_id) <= 2:
            new_id += temp
    return new_id

print(solution(""))