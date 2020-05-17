
def solution(numbers):
    newnumbers = list(map(str, numbers))
    newnumbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(newnumbers)))

Numbers = [
    [6, 10, 2],
    [3, 30, 34, 5, 9]
]

for numbers in Numbers:
    print(solution(numbers))
