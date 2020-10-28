def solution(clothes):
    answer = 1
    clothes_dic = {}
    for n, t in clothes:
        if t in clothes_dic:
            clothes_dic[t] += 1
        else:
            clothes_dic[t] = 1
    for k, v in clothes_dic.items():
        answer *= (v+1)
    return answer - 1


C = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(C))