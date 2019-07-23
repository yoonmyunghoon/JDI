a = input()
d = {'UPPER CASE': 0, 'LOWER CASE': 0}
for i in a:
    if 97<=ord(i)<=122:
        d['LOWER CASE'] += 1
    elif 65<=ord(i)<=90:
        d['UPPER CASE'] += 1
for k,v in d.items():
    print('{} {}'.format(k, v))