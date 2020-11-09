import collections

text = "gaalllsesdfdfsadfd"
Couter_ = collections.Counter(text)
print(Couter_)
for k, v in Couter_.items():
    print(k, v)

import heapq
arr = [1,2,3,3,5,2,5,4,4,3,2]
heapq.heapify(arr)
print(arr)
heapq.heappop(arr)
print(arr)
heapq.heappush(arr, 8)
print(arr)
heapq.heapreplace(arr, 3)
print(arr)