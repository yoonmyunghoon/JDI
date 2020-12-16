from math import gcd


def solution(w, h):
    answer = 1
    gcd_ = gcd(w, h)
    x = w//gcd_
    y = h//gcd_
    print(x, y)
    x_ = x // 2
    y_ = y // 2
    print(x_, y_)
    return answer

print(solution(8, 12))
