import sys
sys.stdin = open("1806_부분합.txt")

N, S = map(int, input().split())
data = list(map(int, input().split()))
minimum_l = 100001
start = 0
end = 0
sum_ = data[0]
while 1:
    if start == len(data) - 1 and end == len(data) - 1:
        break
    if end == len(data) - 1:
        sum_ -= data[start]
        start += 1
    else:
        if sum_ < S:
            end += 1
            sum_ += data[end]
        else:
            sum_ -= data[start]
            start += 1
    if sum_ >= S:
        if minimum_l > end - start + 1:
            minimum_l = end - start + 1
if minimum_l != 100001:
    print(minimum_l)
else:
    print(0)