def solution(arr):
    answer = [0, 0]

    def count(a, b, x, y):
        temp = arr[a][b]
        flag = 0
        for i in range(a, x+1):
            if flag == 1:
                break
            for j in range(b, y+1):
                if arr[i][j] != temp:
                    flag = 1
                    break
        if flag == 0:
            answer[temp] += 1
        else:
            h = (x-a+1)//2
            count(a, b, a+h-1, b+h-1)
            count(a, b+h, a+h-1, b+2*h-1)
            count(a+h, b, a+2*h-1, b+h-1)
            count(a+h, b+h, a+2*h-1, b+2*h-1)
    count(0, 0, len(arr)-1, len(arr)-1)
    return answer

A = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(A))