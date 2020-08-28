import sys
sys.stdin = open("9421_소수상근수.txt")


def check(num):
    number = num
    result = []
    while 1:
        if number == 1:
            return 1
        number = divide(number)
        if number in result:
            return 0
        result.append(number)


def divide(num):
    number = num
    result = []
    while 1:
        if int(number//10) == 0:
            result.append(number)
            break
        result.append(number%10)
        number = int(number//10)
    output = 0
    for k in result:
        output += k**2
    return output


n = int(input())
data = [1]*(n+1)
data[0] = 0
data[1] = 0

for i in range(4, n+1, 2):
    data[i] = 0
for i in range(3, int(n**0.5)+1, 2):
    if data[i]:
        for j in range(i*i, n+1, i*2):
            data[j] = 0
for i in range(len(data)):
    if data[i] == 1:
        if check(i) == 1:
            print(i)