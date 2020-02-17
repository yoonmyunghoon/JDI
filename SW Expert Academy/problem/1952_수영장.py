import sys
sys.stdin = open("1952_수영장.txt")

def cal(n, cost):
    global plan, minimum
    if n > 11:
        if minimum > cost:
            minimum = cost
        return
    if plan[n] > 0:
        cal(n+1, cost+costs[0]*plan[n])
        cal(n+1, cost+costs[1])
        cal(n+3, cost+costs[2])
    else:
        cal(n+1, cost)


T = int(input())
for tc in range(1, T+1):
    costs = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    minimum = 987654321
    cal(0, 0)
    print('#{} {}'.format(tc, min(minimum, costs[3])))