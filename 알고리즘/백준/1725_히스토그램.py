import sys
sys.stdin = open("1725_히스토그램.txt")


def histogram(s, e):
    if s == e:
        return data[s]
    mid = (s+e)//2
    result = max(histogram(s, mid), histogram(mid+1, e))
    left = mid
    right = mid
    height = data[mid]
    length = 1
    ret = height*length
    while 1:
        if left == s and right == e:
            break
        if left == s and right < e:
            height = min(data[right + 1], height)
            length += 1
            right += 1
        elif right == e and left > s:
            height = min(data[left - 1], height)
            length += 1
            left -= 1
        else:
            if data[left-1] > data[right+1]:
                height = min(data[left-1], height)
                length += 1
                left -= 1
            else:
                height = min(data[right + 1], height)
                length += 1
                right += 1
        ret = max(ret, height*length)
    return max(ret, result)


N = int(input())
data = [int(input()) for _ in range(N)]
print(histogram(0, N-1))
