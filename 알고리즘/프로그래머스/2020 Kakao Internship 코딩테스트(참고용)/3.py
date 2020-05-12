def chk(i, gems):
    if not i:
        return False
    # i길이인 슬라이드
    tmp = dict()
    for j in range(i):
        if tmp.get(gems[j]):
            tmp[gems[j]] += 1
        else:
            tmp[gems[j]] = 1
    if len(tmp) == gem_count:
        return True
    # 5개인데 길이3이면 0, 1, 2 이렇게 네개나옴
    #                   2, 3, 4
    for j in range(len(gems) - i):
        # 현재인덱스 빼고 i+j인덱스 더한다
        tmp[gems[j]] -= 1
        if not tmp[gems[j]]:
            del tmp[gems[j]]
        if tmp.get(gems[j + i]):
            tmp[gems[j + i]] += 1
        else:
            tmp[gems[j + i]] = 1
        if len(tmp) == gem_count:
            return True
    return False

def chk2(i, gems):
    if not i:
        return False
    # i길이인 슬라이드
    tmp = dict()
    for j in range(i):
        if tmp.get(gems[j]):
            tmp[gems[j]] += 1
        else:
            tmp[gems[j]] = 1
    if len(tmp) == gem_count:
        return [1, i]
    # 5개인데 길이3이면 0, 1, 2 이렇게 네개나옴
    #                   2, 3, 4
    for j in range(len(gems) - i):
        # 현재인덱스 빼고 i+j인덱스 더한다
        tmp[gems[j]] -= 1
        if not tmp[gems[j]]:
            del tmp[gems[j]]
        if tmp.get(gems[j + i]):
            tmp[gems[j + i]] += 1
        else:
            tmp[gems[j + i]] = 1
        if len(tmp) == gem_count:
            return [j+2, i+j+1]

def bs(s, e, gems):
    if s == e:
        return s
    m = (s + e) // 2
    if chk(m, gems):
        return bs(s, m, gems)
    else:
        return bs(m + 1, e, gems)


def solution(gems):
    global gem_count
    gem_count = len(set(gems))
    answer = chk2(bs(0, len(gems), gems), gems)
    return answer

solution(["XYZ", "XYZ", "XYZ"])
solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])