def solution(numbers):
    arr = list(map(str, numbers))
    set_ = set()

    def perm(n, r):
        if r == 0:
            set_.add(int(''.join(T)))
            return
        else:
            for i in range(n-1, -1, -1):
                arr[i], arr[n-1] = arr[n-1], arr[i]
                T[r-1] = arr[n-1]
                perm(n-1, r-1)
                arr[i], arr[n-1] = arr[n-1], arr[i]

    for i in range(1, len(numbers)+1):
        T = [0]*i
        perm(len(numbers), i)

    result = list(set_)
    answer = 0
    for number in result:
        if number >= 2:
            flag = 0
            for i in range(2, int(number**0.5)+1):
                if number % i == 0:
                    flag = 1
                    break
            if flag == 0:
                answer += 1
    return answer


N = "011"
print(solution(N))
