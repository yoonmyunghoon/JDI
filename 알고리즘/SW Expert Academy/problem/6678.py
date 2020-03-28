# l = []
# while True:
#     i = input()
#     if i != '':
#         l.append(i.upper())
#     else:
#         break
# for i in l:
#     print('>> {}'.format(i))


l = []
for i in range(3):
    i = input()
    l.append(i.upper())
for i in l:
    print('>> {}'.format(i))