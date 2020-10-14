import sys
sys.stdin = open("2038_골롱 수열.txt")

n = int(input())
if n == 1:
    print(1)
else:
    sum_ = [0, 1]
    k = 1
    for i in range(2, n+1):
        if sum_[k] < i:
            k += 1
        sum_.append(sum_[i-1] + k)
        if sum_[i] >= n:
            print(i)
            break



# i 1 2 3 4 5 6 7 8 9 10
# k 1 2 2 3 3 4 4 4 5 5
# s 1 3 5 8 11 15 19 23 28 33