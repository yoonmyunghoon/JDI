arr = [2, 6, 4, 7, 10, 9]
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    result = quick_sort(less) + [pivot] + quick_sort(greater)
    return result
print(quick_sort(arr))

