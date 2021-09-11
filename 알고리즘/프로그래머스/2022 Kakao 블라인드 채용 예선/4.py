from itertools import combinations_with_replacement


def solution(n, info):

    def cal_score(lion_info):
        apeach_score = 0
        lion_score = 0
        for p in range(11):
            if info[p] == 0 and lion_info[p] == 0:
                continue
            else:
                if info[p] >= lion_info[p]:
                    apeach_score += (10-p)
                else:
                    lion_score += (10-p)
        if apeach_score < lion_score:
            return lion_score - apeach_score
        else:
            return 0

    answer = []
    max_result = 0
    scores = range(11)
    selected_list = list(combinations_with_replacement(scores, n))
    for selected in selected_list:
        compare_info = [0]*11
        for i in selected:
            compare_info[10-i] += 1
        result_score = cal_score(compare_info)
        if result_score != 0:
            if result_score > max_result:
                max_result = result_score
                answer = compare_info
            elif result_score == max_result:
                flag = 0
                for x in range(11):
                    if answer[10 - x] < compare_info[10 - x]:
                        flag = 1
                        break
                    elif answer[10 - x] > compare_info[10 - x]:
                        flag = 0
                        break
                if flag == 1:
                    answer = compare_info
    if max_result == 0:
        return [-1]
    else:
        return answer


n_ex = 10
info_ex = [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n_ex, info_ex))