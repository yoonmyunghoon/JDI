def solution(numbers):
    new_numbers = list(map(str, numbers))
    new_numbers.sort(key=lambda x: x*3, reverse=True)
    new_numbers = str(int(''.join(new_numbers)))
    return new_numbers

N = [3, 30, 34, 5, 9, 0]
N1 = [0, 0, 0]
print(solution(N1))
