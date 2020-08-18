import sys
sys.stdin = open("2037_문자메시지.txt")

p, w = map(int, input().split())
words = input()
data = '0 ADGJMPTW00BEHKNQUX00CFILORVY0000000S0Z'
time = 0
namergy = 0

for i in range(len(words)):
    mock = data.index(words[i]) // 10
    if i == 0:
        namergy = data.index(words[i]) % 10
        time = time + (p * (mock + 1))
    else:
        if namergy == data.index(words[i]) % 10:
            if namergy == 1:
                time = time + (p * (mock + 1))
            else:
                time = time + (p * (mock + 1)) + w
        else:
            namergy = data.index(words[i]) % 10
            time = time + (p * (mock + 1))
print(time)