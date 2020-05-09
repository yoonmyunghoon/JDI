
def solution(gems):
    gems_dic = {}
    for gem in gems:
        if gems_dic.get(gem):
            gems_dic[gem] += 1
        else:
            gems_dic[gem] = 1
    orderbyvalue = sorted(gems_dic.items(), key=lambda x: x[1])
    prior_gems = []
    for g, c in orderbyvalue:
        prior_gems.append(g)
    gems_set = set(gems)
    for size in range(len(gems_set), len(gems)+1):
        for i in range(len(gems) - size + 1):
            for prior_gem in prior_gems:
                if prior_gem not in gems[i:i+size]:
                    break
            if set(gems[i:i+size]) == gems_set:
                return [i+1, i+size]

gemss = [
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
    ["AA", "AB", "AC", "AA", "AC"],
    ["XYZ", "XYZ", "XYZ"],
    ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
]

for gems in gemss:
    print(solution(gems))