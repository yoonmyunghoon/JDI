import math
a = input().split(', ')
lis = [str(round(int(r)*2*math.pi, 2)) for r in a]
print(', ' .join(lis))