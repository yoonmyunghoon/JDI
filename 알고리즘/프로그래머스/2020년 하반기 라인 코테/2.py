def solution(ball, order):
    answer = []
    check = [0]*len(ball)
    s = 0
    e = len(ball) - 1
    n = 0
    while e - s != -1:
        if check[s] == 1:
            answer.append(ball[s])
            s += 1
            continue
        if check[e] == 1:
            answer.append(ball[e])
            e -= 1
            continue
        if ball[s] == order[n]:
            answer.append(ball[s])
            n += 1
            s += 1
        elif ball[e] == order[n]:
            answer.append(ball[e])
            n += 1
            e -= 1
        else:
            b_idx = ball.index(order[n])
            n += 1
            check[b_idx] = 1
    return answer

Ball = [11, 2, 9, 13, 24]
Order = [9, 2, 13, 24, 11]
print(solution(Ball, Order))