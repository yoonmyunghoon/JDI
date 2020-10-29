import collections


def solution(bridge_length, weight, truck_weights):
    deq = collections.deque()
    now_count = 0
    now_weight = 0
    t = 0
    passed = 0
    truck_cnt = len(truck_weights)
    idx = 0
    while 1:
        if passed == truck_cnt:
            break
        t += 1
        if len(deq) != 0 and deq[0][1] == t:
            x = deq.popleft()
            passed += 1
            now_count -= 1
            now_weight -= x[0]
        if idx < truck_cnt and now_count+1 <= bridge_length and now_weight + truck_weights[idx] <= weight:
            deq.append((truck_weights[idx], t+bridge_length))
            now_count += 1
            now_weight += truck_weights[idx]
            idx += 1
    return t


B = 100
W = 100
T = [10,10,10,10,10,10,10,10,10,10]
print(solution(B, W, T))