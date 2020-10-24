def solution(answers):
    answer = []
    soopo_1 = [1, 2, 3, 4, 5]
    soopo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    soopo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]

    answers_len = len(answers)
    for i in range(answers_len):
        temp = answers[i]
        if temp == soopo_1[i%5]:
            scores[0] += 1
        if temp == soopo_2[i%8]:
            scores[1] += 1
        if temp == soopo_3[i%10]:
            scores[2] += 1
    max_score = max(scores)
    for i in range(3):
        if max_score == scores[i]:
            answer.append(i+1)
    return answer

A = [1,2,3,4,5]
print(solution(A))