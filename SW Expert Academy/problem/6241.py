url = input()
url = url.replace('://', ' ')
url = url.replace('/', ' ')
l = url.split(' ')
r = ['protocol', 'host', 'others']
d = {i: j for i, j in zip(r, l)}
for k,v in d.items():
    print('{}: {}'.format(k, v))