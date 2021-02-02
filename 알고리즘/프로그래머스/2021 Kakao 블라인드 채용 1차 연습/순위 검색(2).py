data_list = [['cpp', 'java', 'python', '-'],
                 ['backend', 'frontend', '-'],
                 ['junior', 'senior', '-'],
                 ['chicken', 'pizza', '-']]
initial_dict = {}
cnt = 0


def make_dict(d, key_name):
    if d == 4:
        initial_dict[key_name] = []
        return
    else:
        for t in data_list[d]:
            make_dict(d+1, key_name+t)


def insert_data(d, key_name, line):
    if d == 4:
        initial_dict[key_name].append(int(line[4]))
    else:
        insert_data(d+1, key_name+'-', line)
        insert_data(d+1, key_name+line[d], line)


def lower_bound(s, e, target_num, arr):
    global cnt
    if s == e:
        cnt = len(arr) - s
    else:
        mid = (s+e)//2
        if target_num <= arr[mid]:
            lower_bound(s, mid, target_num, arr)
        else:
            lower_bound(mid+1, e, target_num, arr)


def solution(info, query):
    global cnt
    answer = []

    make_dict(0, '')

    for info_line in info:
        new_line = list(info_line.split())
        insert_data(0, '', new_line)

    for v in initial_dict.values():
        v.sort()

    for q in query:
        nq = q.replace('and ', '')
        nq = list(nq.split())
        key_name = nq[0]+nq[1]+nq[2]+nq[3]
        score = int(nq[4])
        check_list = initial_dict[key_name]
        check_list_len = len(check_list)
        cnt = 0
        if check_list_len != 0:
            if check_list[0] >= score:
                cnt = check_list_len
            elif check_list[-1] < score:
                cnt = 0
            else:
                lower_bound(0, check_list_len-1, score, check_list)
        answer.append(cnt)
    return answer


Info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]
Query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(Info, Query))


