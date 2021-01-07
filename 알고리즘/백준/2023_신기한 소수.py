import sys
sys.stdin = open("2023_신기한 소수.txt")


def prime_check(number):
    for i in range(3, int(number**0.5)+1, 2):
        if number % i == 0:
            return 0
    return 1


def amazing_prime_check(depth):
    if depth == N:
        print(int(''.join(amazing_prime)))
    elif depth == 0:
        for a in range(4):
            amazing_prime[0] = first_nums[a]
            amazing_prime_check(depth + 1)
    else:
        for b in range(4):
            amazing_prime[depth] = nums[b]
            if prime_check(int(''.join(amazing_prime[:depth+1]))):
                amazing_prime_check(depth + 1)


N = int(input())
first_nums = ['2', '3', '5', '7']
nums = ['1', '3', '7', '9']
amazing_prime = ['-1']*N
amazing_prime_check(0)