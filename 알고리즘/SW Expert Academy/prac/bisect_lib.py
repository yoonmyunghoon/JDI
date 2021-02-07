from bisect import bisect_left, bisect_right

a = [1, 2, 2, 3, 3, 5, 5, 5, 7, 8, 8, 9, 9, 9, 14, 25, 32, 32, 55]
print(bisect_left(a, 4))
print(bisect_right(a, 5))


def count_by_range(left_value, right_value):
    return bisect_right(a, right_value) - bisect_left(a, left_value)


print(count_by_range(3, 6))
