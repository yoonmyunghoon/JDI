import sys
sys.stdin = open("1629_곱셈.txt")


def square(k, number):
    if k == 1:
        return number % C
    temp = square(k // 2, number) % C
    if k % 2 == 0:
        return (temp * temp) % C
    else:
        return (temp * temp * number) % C


A, B, C = map(int, input().split())
print(square(B, A))