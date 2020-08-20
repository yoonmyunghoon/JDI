import sys
sys.stdin = open("1331_나이트 투어.txt")


def diff(a, b):
    if a > b:
        return a - b
    else:
        return b - a


path = []
result = 1
for i in range(36):
    p = input()
    path.append(p)

# 중복체크
s_path = set(path)
c_path = list(s_path)
if len(s_path) != len(path):
    result = 0
else:
    # 끝점체크
    dx = diff(int(path[35][1]), int(path[0][1]))
    dy = diff(ord(path[35][0]), ord(path[0][0]))
    if dx * dy != 2 or dx + dy != 3:
        result = 0
    else:
        # 경로체크
        for i in range(35):
            now = path[i]
            after = path[i+1]
            dx = diff(int(now[1]), int(after[1]))
            dy = diff(ord(now[0]), ord(after[0]))
            if dx * dy != 2 or dx + dy != 3:
                result = 0
                break

if result == 1:
    print('Valid')
else:
    print('Invalid')