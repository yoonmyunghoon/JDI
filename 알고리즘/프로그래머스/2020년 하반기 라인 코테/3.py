minimum = 987654321
result = -1


def recursion(num_str, num_len, cnt):
    global minimum, result
    if cnt >= minimum:
        return
    if num_len == 1:
        if cnt < minimum:
            minimum = cnt
            result = int(num_str)
        return
    for i in range(num_len - 1):
        l_num = int(num_str[:i + 1])
        r_num = int(num_str[i + 1:])
        l_num_c = str(l_num)
        r_num_c = str(r_num)
        if len(l_num_c) + len(r_num_c) == num_len:
            new_num = l_num + r_num
            new_num = str(new_num)
            recursion(new_num, len(new_num), cnt + 1)


def solution(n):
    global minimum, result
    n_str = str(n)
    recursion(n_str, len(n_str), 0)
    answer = [minimum, result]
    return answer

N = 73425
print(solution(N))