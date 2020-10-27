def solution(numbers, target):
    def calculator(n, result, length):
        if n == length:
            if result == target:
                return 1
            return 0
        else:
            return calculator(n+1, result+numbers[n], length) + calculator(n+1, result-numbers[n], length)
    answer = calculator(0, 0, len(numbers))
    return answer

N = [1, 1, 1, 1, 1]
T = 3
print(solution(N, T))