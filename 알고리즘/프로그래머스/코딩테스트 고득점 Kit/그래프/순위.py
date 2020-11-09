def solution(n, results):
    answer = 0
    winners = [set() for x in range(n + 1)]  # x에게 이긴 선수들
    losers = [set() for x in range(n + 1)]  # x에게 진 선수들
    for winner, loser in results:
        winners[loser].add(winner)
        losers[winner].add(loser)
    for i in range(1, n + 1):
        for j in winners[i]:
            losers[j] = losers[j].union(losers[i])
        for k in losers[i]:
            winners[k] = winners[k].union(winners[i])
    for i in range(1, n + 1):
        if len(losers[i]) + len(winners[i]) == n - 1:
            answer += 1

    return answer