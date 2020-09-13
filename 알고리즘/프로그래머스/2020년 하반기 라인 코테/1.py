def solution(boxes):
    dic = {}
    for i in range(len(boxes)):
        for j in range(2):
            if boxes[i][j] in dic:
                dic[boxes[i][j]] += 1
            else:
                dic[boxes[i][j]] = 1
    count = 0
    for k, v in dic.items():
        if v % 2:
            count += 1
    answer = count//2
    print(dic)
    return answer


Boxes = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]
print(solution(Boxes))