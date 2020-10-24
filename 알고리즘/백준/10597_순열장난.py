import sys
sys.stdin = open("10597_순열장난.txt")


def find_array(s):
    if s == len(numbers) - 1:
        print(array)
        return
    if numbers[s] == "0":
        return
    if int(numbers[s:s+1]) > N:
        return
    if numbers[s:s+1] not in array:
        array.append(numbers[s:s+1])
        find_array(s+1)
        array.pop()
    else:
        if int(numbers[s:s+2]) > N:
            return
        if numbers[s:s + 2] not in array:
            array.append(numbers[s:s+2])
            find_array(s+2)
            array.pop()


numbers = input()
numbers_len = len(numbers)
N = 1
if numbers_len <= 9:
    N = numbers_len
else:
    N = 9 + (numbers_len - 9)//2
print(N)
array = []
find_array(0)
print(array)



# 4121411091587613532
# 4 1 2 14 11 0
