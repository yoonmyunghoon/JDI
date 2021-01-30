from itertools import combinations


def solution(orders, course):
    answer = []
    max_len = 0
    for i in range(len(orders)):
        new_list = list(orders[i])
        new_list.sort()
        orders[i] = ''.join(new_list)
        if len(orders[i]) > max_len:
            max_len = len(orders[i])
    for c in course:
        if c > max_len:
            break
        check_dict = dict()
        for order in orders:
            comb = list(combinations(order, c))
            for x in comb:

                if x not in check_dict:
                    check_dict[x] = 1
                else:
                    check_dict[x] += 1
        Maxim = max(check_dict.values())
        for k, v in check_dict.items():
            if v == Maxim and v >= 2:
                kk = list(k)
                kk.sort()
                answer.append(''.join(kk))
    answer.sort()
    return answer


Orders = ["XYZ", "XWY", "WXA"]
Course = [2,3,4]
print(solution(Orders, Course))