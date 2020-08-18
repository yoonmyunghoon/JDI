import sys
sys.stdin = open("2037_문자메시지.txt")

p, w = map(int, input().split())
words = input()
data = {
    ' ': [1, 1],
    'A': [2, 1],
    'B': [2, 2],
    'C': [2, 3],
    'D': [3, 1],
    'E': [3, 2],
    'F': [3, 3],
    'G': [4, 1],
    'H': [4, 2],
    'I': [4, 3],
    'J': [5, 1],
    'K': [5, 2],
    'L': [5, 3],
    'M': [6, 1],
    'N': [6, 2],
    'O': [6, 3],
    'P': [7, 1],
    'Q': [7, 2],
    'R': [7, 3],
    'S': [7, 4],
    'T': [8, 1],
    'U': [8, 2],
    'V': [8, 3],
    'W': [9, 1],
    'X': [9, 2],
    'Y': [9, 3],
    'Z': [9, 4]
}
time = 0
flag = 1

for s in words:
    if flag == data[s][0]:
        if flag != 1:
            time = time + (p * data[s][1]) + w
        else:
            time = time + (p * data[s][1])
    else:
        flag = data[s][0]
        time = time + (p * data[s][1])
print(time)