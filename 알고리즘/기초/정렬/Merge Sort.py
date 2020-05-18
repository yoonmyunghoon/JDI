arr = [2, 6, 4, 7, 10, 9]

def merge(left, right):
    i = 0
    j = 0
    sorted_list = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    return sorted_list

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr)//2
    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])
    return merge(left, right)

print(merge_sort(arr))