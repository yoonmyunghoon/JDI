import math
a = float(input())
b = float(input())
c = float(input())
def my_sqrt(a, b, c):
    if math.isclose(a**2, b) and math.isclose(c**2, b):
        return a, c
    else:
        if a**2 <= b <= c**2:
            if ((a+c)/2)**2 <= b < c**2:
                return my_sqrt((a+c)/2, b, c)
            else:
                return my_sqrt(a, b, (a+c)/2)

print(my_sqrt(a, b, c))

# import math
# n = float(input())
# def my_sqrt(n):
#     a = 1
#     b = n
#     while math.isclose(a**2, n) == False:
#         if a**2 <= n < b**2:
#             if n <= ((a+b)/2)**2 < b**2:
#                 b = (a+b)/2
#             else:
#                 a = (a+b)/2
#     return a, b

# print(my_sqrt(n))

