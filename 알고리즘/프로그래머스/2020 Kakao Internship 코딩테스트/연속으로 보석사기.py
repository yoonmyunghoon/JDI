import collections, copy

def cal(gems, gems_dic):
    start = 0
    end = len(gems) - 1
    while 1:
        if gems_dic[gems[-1]] > 1:
            gems_dic[gems[-1]] -= 1
            gems.pop()
            end -= 1
        else:
            break
    while 1:
        if gems_dic[gems[0]] > 1:
            gems_dic[gems[0]] -= 1
            gems.popleft()
            start += 1
        else:
            break
    return [start, end]


def cal_ot(gems):
    gems_set = set(gems)
    for size in range(len(gems_set), len(gems)+1):
        for i in range(len(gems) - size + 1):
            if set(gems[i:i+size]) == gems_set:
                return [i+1, i+size]


def solution(gems):
    gems_deq = collections.deque(gems)
    gems_dic = {}
    for gem in gems:
        if gems_dic.get(gem):
            gems_dic[gem] += 1
        else:
            gems_dic[gem] = 1
    s2, e2 = cal(copy.deepcopy(gems_deq), copy.deepcopy(gems_dic))
    ts, te = cal_ot(gems[s2:e2 + 1])
    return [s2 + ts, s2 + te]

gemss = [
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
    ["AA", "AB", "AC", "AA", "AC"],
    ["XYZ", "XYZ", "XYZ"],
    ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
]

for gems in gemss:
    print(solution(gems))