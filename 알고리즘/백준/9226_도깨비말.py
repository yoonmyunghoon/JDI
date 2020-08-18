import sys
sys.stdin = open("9226_도깨비말.txt")

while 1:
    words = input()
    checkpoint = 0
    if words == '#':
        break
    else:
        for i in range(len(words)):
            if words[i] in 'aeiou':
                checkpoint = i
                break
        print(words[checkpoint:] + words[:checkpoint] + 'ay')