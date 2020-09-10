def solution(numbers):
    answer = set()
    for i in range(len(numbers)-1):
        for j in range(i, len(numbers)):
            if i != j:
                answer.add(numbers[i]+numbers[j])
    answer = list(answer)
    answer.sort()
    return answer