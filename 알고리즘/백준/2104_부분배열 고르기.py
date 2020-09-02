import sys
sys.stdin = open("2104_부분배열 고르기.txt")

def finding(s, e, n):
    if n == 1:
        return A[s], A[s], A[s]*A[s]
    else:
        l_min, l_sum, l_result = finding(s, e-1, n-1)
        r_min, r_sum, r_result = finding(s+1, e, n-1)
        Min = min(l_min, r_min)
        Sum = l_sum + A[e]
        Max_result = max(l_result, r_result, Min*Sum)
        return Min, Sum, Max_result


N = int(input())
A = list(map(int, input().split()))
print(finding(0, N-1, N)[2])
