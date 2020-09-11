def solution(a):
    answer = 0
    if len(a) < 3:
        answer = len(a)
    else:
        left = [0]*len(a)
        right = [0]*len(a)
        left_min = a[0]
        right_min = a[-1]
        for i in range(len(a)):
            if left_min > a[i]:
                left_min = a[i]
            left[i] = left_min
        for j in range(len(a)-1, -1, -1):
            if right_min > a[j]:
                right_min = a[j]
            right[j] = right_min
        for k in range(len(a)):
            if left[k] < a[k] and right[k] < a[k]:
                answer += 1
        answer = len(a) - answer
    return answer

# print(solution([-16, 27, 65, -2, 58, -92, -72, -68, -41, -33]))
print(solution([9,-1,-5]))