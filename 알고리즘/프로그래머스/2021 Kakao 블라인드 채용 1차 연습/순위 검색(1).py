initial_dict = {}
data_list = [['cpp', 'java', 'python'], ['backend', 'frontend'], ['junior', 'senior'], ['chicken', 'pizza']]
cnt = 0


def make_dict(d, dic):
    if d == 3:
        dic['chicken'] = []
        dic['pizza'] = []
    else:
        for i in data_list[d]:
            dic[i] = {}
            make_dict(d + 1, dic[i])


def count_result(d, dic, L):
    global cnt
    if d == 3:
        if L[d] == '-':
            for i in data_list[d]:
                for j in dic[i]:
                    if j >= L[4]:
                        cnt += 1
        else:
            for j in dic[L[d]]:
                if j >= L[4]:
                    cnt += 1
    else:
        if L[d] == '-':
            for i in data_list[d]:
                count_result(d+1, dic[i], L)
        else:
            count_result(d+1, dic[L[d]], L)


def solution(info, query):
    global cnt
    answer = []
    make_dict(0, initial_dict)

    for data in info:
        l, w, e, f, s = data.split()
        initial_dict[l][w][e][f].append(int(s))

    for q in query:
        nq = q.replace('and ', '')
        nq_list = list(nq.split())
        nq_list[4] = int(nq_list[4])
        cnt = 0
        count_result(0, initial_dict, nq_list)
        answer.append(cnt)

    return answer


Info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
Query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(Info, Query))


