s = 'abcdefgabc'
d = {}
for i in s:
    d[i] = s.count(i)
for k,v in d.items():
    print('{},{}'.format(k,v))