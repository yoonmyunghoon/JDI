T = int(input())
for test_case in range(T):
    N = int(input())
    baselist = [[0]*10 for i in range(11)]
    for i in range(N):
        lis = list(map(int, input().split()))
        if lis[4] == 1:
            for x in range(lis[0], lis[2]+1):
                for y in range(lis[1], lis[3]+1):
                    baselist[x][y] = 1
        else:   
            for x in range(lis[0], lis[2]+1):
                for y in range(lis[1], lis[3]+1):
                    if baselist[x][y] == 1:
                        baselist[x][y] = 3
                    else:
                        baselist[x][y] = 2
    count = 0
    for i in baselist:
        # print(i)
        count += i.count(3)
    print('#{} {}'.format(test_case+1, count))
    


