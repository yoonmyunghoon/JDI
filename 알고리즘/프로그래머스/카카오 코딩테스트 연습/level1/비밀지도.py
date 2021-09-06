def solution(n, arr1, arr2):

    def change_number(x):
        if len(x) != n:
            x = (n - len(x))*'0' + x
        return x

    answer = []
    for i in range(n):
        a = bin(arr1[i])[2:]
        b = bin(arr2[i])[2:]
        a = change_number(a)
        b = change_number(b)
        c = ''
        for j in range(n):
            if a[j] == '0' and b[j] == '0':
                c += ' '
            else:
                c += '#'
        answer.append(c)
    return answer


n_ex = 5
arr1_ex = [9, 20, 28, 18, 11]
arr2_ex = [30, 1, 21, 17, 28]

print(solution(n_ex, arr1_ex, arr2_ex))