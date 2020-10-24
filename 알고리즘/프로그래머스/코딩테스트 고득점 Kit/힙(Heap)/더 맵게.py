import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while 1:
        if len(scoville) == 1:
            if scoville[0] < K:
                answer = -1
            break
        else:
            a = heapq.heappop(scoville)
            if a >= K:
                break
            else:
                b = heapq.heappop(scoville)
                c = a + b*2
                heapq.heappush(scoville, c)
                answer += 1
    return answer

S = [1, 2, 3, 9, 10, 12]
S1 = [3, 2, 55, 1, 6, 22, 753]
K = 7

print(solution(S, K))