import sys, itertools
sys.stdin = open("6603_로또.txt")

while 1:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    S = data[1:]
    result = list(itertools.combinations(S, 6))
    for line in result:
        for num in line:
            print(num, end=' ')
        print()
    print()