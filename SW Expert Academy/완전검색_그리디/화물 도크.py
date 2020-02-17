import sys
sys.stdin = open("화물 도크.txt")

T = int(input())
for tc in range(1, T+1):
   N = int(input())
   arr = [[0 for _ in range(2)] for _ in range(N)]
   for i in range(N):
       s, e =  list(map(int, input().split()))
       arr[i] = [e, s]
   arr.sort()
   new_s = arr[0][1]
   new_e = arr[0][0]
   cnt = 1
   for i in range(1, len(arr)):
       s = arr[i][1]
       e = arr[i][0]
       if new_e <= s:
           new_e = e
           new_s = s
           cnt += 1
   print('#{} {}'.format(tc, cnt))