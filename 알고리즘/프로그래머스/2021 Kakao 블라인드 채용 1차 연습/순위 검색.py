def solution(info, query):
    answer = []
    lang_type = [set(), set(), set()]
    work_type = [set(), set()]
    exp_type = [set(), set()]
    food_type = [set(), set()]
    scores = [0] * len(info)

    for i in range(len(info)):
        a_info = list(info[i].split())

        if a_info[0] == 'cpp':
            lang_type[0].add(i)
        elif a_info[0] == 'java':
            lang_type[1].add(i)
        else:
            lang_type[2].add(i)

        if a_info[1] == 'backend':
            work_type[0].add(i)
        else:
            work_type[1].add(i)

        if a_info[2] == 'junior':
            exp_type[0].add(i)
        else:
            exp_type[1].add(i)

        if a_info[3] == 'chicken':
            food_type[0].add(i)
        else:
            food_type[1].add(i)

        scores[i] = int(a_info[4])

    for i in range(len(query)):
        q = list(query[i].replace('and ', '').split())
        if q[0] == 'cpp': a = 0
        elif q[0] == 'java': a = 1
        elif q[0] == 'python': a = 2
        else: a = -1

        if q[1] == 'backend': b = 0
        elif q[1] == 'frontend': b = 1
        else: b = -1

        if q[2] == 'junior': c = 0
        elif q[2] == 'senior': c = 1
        else: c = -1

        if q[3] == 'chicken': d = 0
        elif q[3] == 'pizza': d = 1
        else: d = -1

        check = [a, b, c, d]
        result = set(range(len(info)))
        for k in range(4):
            if check[k] == -1:
                continue
            else:
                if k == 0:
                    result = result.intersection(lang_type[check[k]])
                elif k == 1:
                    result = result.intersection(work_type[check[k]])
                elif k == 2:
                    result = result.intersection(exp_type[check[k]])
                else:
                    result = result.intersection(food_type[check[k]])
        cnt = 0
        for s in result:
            if scores[s] >= int(q[4]):
                cnt += 1
        answer.append(cnt)
    return answer


Info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
Query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(Info, Query))


