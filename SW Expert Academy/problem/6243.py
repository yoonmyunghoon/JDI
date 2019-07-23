s = input()
s = s.split(' ')
a = set()
for i in s:
    a.add(i)
print(','.join(sorted(a)))