from itertools import combinations


def solution(orders, course):
    answer = []
    for co in course:
        dic = {}
        for order in orders:
            order_l = list(order)
            order_l.sort()
            order = ''.join(order_l)
            res = list(combinations(order, co))
            for r in res:
                if r in dic:
                    dic[r] += 1
                else:
                    dic[r] = 1
        if len(dic) > 0:
            max_count = max(dic.values())
            if max_count >= 2:
                for k, v in dic.items():
                    if v == max_count:
                        k_list = list(k)
                        k_list.sort()
                        k_str = ''.join(k_list)
                        answer.append(k_str)
    answer.sort()
    return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))