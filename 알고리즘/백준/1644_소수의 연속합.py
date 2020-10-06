import sys, math
sys.stdin = open("1644_소수의 연속합.txt")


def check_prime(n):
    prime_numbers = []
    data = [1] * (n + 1)
    data[0] = 0
    data[1] = 0
    for i in range(4, n + 1, 2):
        data[i] = 0
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if data[i] == 0:
            continue
        else:
            for j in range(i * i, n + 1, i * 2):
                data[j] = 0
    for i in range(n + 1):
        if data[i] == 1:
            prime_numbers.append(i)
    return prime_numbers


def counting(number, prime_d):
    count = 0
    start = 0
    end = 0
    result = prime_d[0]
    length = len(prime_d)
    while 1:
        if end == length-1 and start == length - 1:
            if result == number:
                count += 1
            break
        else:
            if result < number:
                end += 1
                result += prime_d[end]
            elif result == number:
                count += 1
                result -= prime_d[start]
                start += 1
            else:
                result -= prime_d[start]
                start += 1
    return count


N = int(input())
if N == 1:
    print(0)
else:
    prime_data = check_prime(N)
    print(counting(N, prime_data))
