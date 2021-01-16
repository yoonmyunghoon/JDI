import sys
sys.stdin = open("2661_좋은수열.txt")


def find_good_num(d):
    if d > 1:
        check = d//2
        for k in range(1, check+1):
            if array[d-2*k:d-k] == array[d-k:d]:
                return
    if d == N:
        print(''.join(map(str, array)))
        sys.exit()
    else:
        for i in range(1, 4):
            array[d] = i
            find_good_num(d+1)


N = int(input())
array = [0]*N
find_good_num(0)