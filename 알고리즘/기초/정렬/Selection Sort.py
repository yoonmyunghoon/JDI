arr = [2, 6, 4, 7, 10, 9]
n = len(arr)
for i in range(n-1):
    min_point = i
    for j in range(i+1, n):
        if arr[min_point] > arr[j]:
            min_point = j
    arr[min_point], arr[i] = arr[i], arr[min_point]
print(arr)