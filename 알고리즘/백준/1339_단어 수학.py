import sys
sys.stdin = open("1339_단어 수학.txt")

N = int(input())
numbers = [list(input()) for _ in range(N)]
score = dict()
for i in range(N):
    for j in range(len(numbers[i])):
        if numbers[i][j] in score:
            score[numbers[i][j]] += 10 ** (len(numbers[i]) - j - 1)
        else:
            score[numbers[i][j]] = 10 ** (len(numbers[i]) - j - 1)

score_list = []
for k, v in score.items():
    score_list.append([v, k])
score_list.sort(reverse=True)
num = 9
for s in score_list:
    s[0] = num
    num -= 1
for i in range(N):
    for j in range(len(numbers[i])):
        for s in score_list:
            if s[1] == numbers[i][j]:
                numbers[i][j] = s[0]
                break
result = 0
for num in numbers:
    result += int(''.join(map(str, num)))
print(result)
