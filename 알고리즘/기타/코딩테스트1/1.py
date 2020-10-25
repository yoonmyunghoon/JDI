def balancedSum(arr):
    # Write your code here
    sum_ = sum(arr)
    sum_left = 0
    for i in range(1, len(arr)-1):
        sum_left += arr[i-1]
        if sum_left == sum_ - sum_left - arr[i]:
            return i