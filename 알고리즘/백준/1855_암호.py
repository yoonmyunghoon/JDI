import sys
sys.stdin = open("1855_암호.txt")

K = int(input())
word = input()
data = []
cnt = 1
while cnt*K <= len(word):
    if cnt % 2:
        data.append(word[K * (cnt-1):K * cnt])
    else:
        s = word[K * (cnt-1):K * cnt]
        data.append(s[::-1])
    cnt += 1
for i in range(K):
    for j in range(len(word)//K):
        print(data[j][i], end='')