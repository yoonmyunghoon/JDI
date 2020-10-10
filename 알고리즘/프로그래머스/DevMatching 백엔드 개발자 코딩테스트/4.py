def solution(votes, k):
    vote_dict = {}
    vote_list = []
    for v in votes:
        if v in vote_dict:
            vote_dict[v] += 1
        else:
            vote_dict[v] = 1
    for key, val in vote_dict.items():
        vote_list.append([key, val])
    vote_list = sorted(vote_list, key = lambda x : (-x[1], x[0]))
    limit = 0
    for i in range(k):
        limit += vote_list[i][1]
    temp = 0
    idx = len(vote_list) - 1
    while 1:
        temp += vote_list[idx][1]
        if temp >= limit:
            break
        idx -= 1
    answer = vote_list[idx+1][0]
    print(vote_list)
    return answer

Votes = ["AVANT", "PRIDO", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "AVANT", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "SOULFUL", "AVANT", "SANTA"]
Votes1 = ["AAB", "AAA", "AAC", "AAD"]
K = 2
K1 = 4
print(solution(Votes, K))