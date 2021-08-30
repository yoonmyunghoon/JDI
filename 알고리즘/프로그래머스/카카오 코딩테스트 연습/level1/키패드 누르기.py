def solution(numbers, hand):

    def cal_distance(l, r, p, h):
        l_diff = abs(p[0] - l[0]) + abs(p[1] - l[1])
        r_diff = abs(p[0] - r[0]) + abs(p[1] - r[1])
        if l_diff > r_diff:
            return 'R'
        elif l_diff < r_diff:
            return 'L'
        else:
            if h == 'right':
                return 'R'
            else:
                return 'L'

    answer = ''
    positions = [
        (3, 1, '?'),
        (0, 0, 'L'),
        (0, 1, '?'),
        (0, 2, 'R'),
        (1, 0, 'L'),
        (1, 1, '?'),
        (1, 2, 'R'),
        (2, 0, 'L'),
        (2, 1, '?'),
        (2, 2, 'R'),
    ]
    left = (3, 0)
    right = (3, 2)
    for number in numbers:
        if positions[number][2] == '?':
            if cal_distance(left, right, positions[number], hand) == 'L':
                left = positions[number]
                answer += 'L'
            else:
                right = positions[number]
                answer += 'R'

        elif positions[number][2] == 'L':
            left = positions[number]
            answer += 'L'
        else:
            right = positions[number]
            answer += 'R'

    return answer


numbers_ex = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand_ex = "left"
print(solution(numbers_ex, hand_ex))