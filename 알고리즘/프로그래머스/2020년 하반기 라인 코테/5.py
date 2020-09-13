from collections import deque

def solution(cards):
    answer = -1
    for i in range(len(cards)):
        if cards[i] > 10:
            cards[i] = 10
    print(cards)
    cards = deque(cards)
    p_cards = []
    d_cards = []
    score = 0
    while 1:
        if len(cards) == 0:
            break
        else:
            a = cards.popleft()
            c = cards.popleft()
            b = cards.popleft()
            d = cards.popleft()
            if a + b == 21:
                answer += 2
                continue

    return answer

Cards = [12, 7, 11, 6, 2, 12]
print(solution(Cards))