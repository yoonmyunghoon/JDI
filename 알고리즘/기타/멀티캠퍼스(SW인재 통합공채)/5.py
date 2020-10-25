def minX(arr):
    # Write your code here
    min_ = arr[0]
    calc_result = 0
    for i in range(len(arr)):
        calc_result += arr[i]
        if min_ > calc_result:
            min_ = calc_result
    return min_*(-1) + 1