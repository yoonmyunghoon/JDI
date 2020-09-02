import sys
sys.stdin = open("2104_부분배열 고르기.txt")


def finding(s, e):
    if s == e:
        return A[s]*A[s]
    mid = (e+s)//2
    result = max(finding(s, mid), finding(mid + 1, e))
    l = mid
    r = mid
    minimum = A[mid]
    num_sum = minimum
    max_result = minimum*num_sum
    while 1:
        if l == s and r == e:
            break
        if l == s and r < e:
            minimum = min(A[r + 1], minimum)
            num_sum = A[r + 1] + num_sum
            r += 1
        elif r == e and l > s:
            minimum = min(A[l - 1], minimum)
            num_sum = A[l - 1] + num_sum
            l -= 1
        else:
            if (A[l-1]+num_sum)*min(A[l-1], minimum) > (A[r+1]+num_sum)*min(A[r+1], minimum):
                minimum = min(A[l-1], minimum)
                num_sum = A[l-1]+num_sum
                l -= 1
            else:
                minimum = min(A[r+1], minimum)
                num_sum = A[r+1]+num_sum
                r += 1
        max_result = max(max_result, minimum*num_sum)
    return max(result, max_result)


N = int(input())
A = list(map(int, input().split()))
print(finding(0, N-1))