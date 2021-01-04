import sys
sys.stdin = open("10597_순열장난.txt")


def find_array(s):
    global flag
    if flag == 1:
        return
    if s == len_numbers:
        for num in array:
            print(num, end=' ')
        flag = 1
        return
    if numbers[s] not in array:
        array.append(numbers[s])
        find_array(s + 1)
        array.pop()
    if int(numbers[s:s + 2]) <= N and numbers[s:s + 2] not in array:
        array.append(numbers[s:s + 2])
        find_array(s + 2)
        array.pop()


flag = 0
array = []
numbers = input()
len_numbers = len(numbers)
N = 1
if len_numbers < 10:
    N = len_numbers
else:
    N = (len_numbers - 9) // 2 + 9
find_array(0)

