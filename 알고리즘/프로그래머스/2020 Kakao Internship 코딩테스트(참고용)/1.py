def solution(numbers, hand):
    D = {1: 0, 4: 0, 7: 0, 2: 2, 5: 2, 8: 2, 0: 2, 3: 1, 6: 1, 9: 1}
    position = [[1, 3], [0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2], [0, 3], [1, 3], [2, 3]]
    left = [0, 3]
    right = [2, 3]
    answer = []
    for number in numbers:
        if D[number]:
            if D[number] == 1:
                right = position[number]
                answer.append('R')
            else:
                print(number)
                abl = abs(position[number][0] - left[0]) + abs(position[number][1] - left[1])
                abr = abs(position[number][0] - right[0]) + abs(position[number][1] - right[1])
                if abl > abr:
                    right = position[number]
                    answer.append('R')
                elif abl == abr:
                    if hand == "right":
                        right = position[number]
                        answer.append('R')
                    else:
                        left = position[number]
                        answer.append('L')
                else:
                    left = position[number]
                    answer.append('L')
        else:
            left = position[number]
            answer.append('L')
    answer = ''.join(answer)

    return answer