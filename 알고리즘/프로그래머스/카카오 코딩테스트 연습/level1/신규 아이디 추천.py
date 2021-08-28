def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    for c in "~!@#$%^&*()=+[{]}:?,<>/":
        new_id = new_id.replace(c, "")
    # 3
    while 1:
        if new_id.find("..") == -1:
            break
        new_id = new_id.replace("..", ".")
    # 4
    if new_id[0] == ".":
        new_id = new_id[1:]
    if len(new_id):
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    # 5
    if len(new_id) == 0:
        new_id = "a"
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:14]
    # 7
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1]*(3-len(new_id))
    return new_id


new_id_ex = "abcdefghijklmn.p"
print(solution(new_id_ex))