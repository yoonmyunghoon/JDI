import math


def solution(n, k):
    # 진법 변환
    def convert(x, y):
        result_num = ''
        temp = '0123456789ABCDEF'
        while x > 0:
            result_num += temp[int(x % y)]
            x = int(x // y)
        return result_num[::-1]

    # 소수 찾기
    def is_prime_number(num):
        if num == 0 or num == 1:
            return False
        else:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

    changed_num = convert(n, k)
    candidate_list_before = list(changed_num.split('0'))
    candidate_list = []
    for candidate in candidate_list_before:
        if candidate != '':
            candidate_list.append(int(candidate))
    if len(candidate_list) == 0:
        return 0
    else:
        cnt = 0
        for candi in candidate_list:
            if is_prime_number(candi):
                cnt += 1
        return cnt


n_ex = 437674
k_ex = 3
print(solution(n_ex, k_ex))