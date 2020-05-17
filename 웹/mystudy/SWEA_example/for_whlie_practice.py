# for i in range(5):
#     print('*'*i)

# i = 0
# while i <= 4:
#     print('*'*i)
#     i += 1

# for i in range(2):
#     for j in range(1, 5):
#         print('*'*j)

# i = 1
# while i<=2:
#     j = 1
#     while j<=4:
#         print('*'*j)
#         j += 1
#     i += 1

i, k = 5, 1
while i >= 0:
    print('{}{}' .format(' '*i, '*'*(2*k-1)))
    i -= 1
    k += 1