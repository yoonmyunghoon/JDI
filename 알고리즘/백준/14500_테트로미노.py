import sys
sys.stdin = open("14500_테트로미노.txt")


def four():
    global maximum
    for i in range(N):
        for j in range(M-3):
            hap = data[i][j] + data[i][j+1] + data[i][j+2] + data[i][j+3]
            if hap > maximum:
                maximum = hap
    for j in range(M):
        for i in range(N-3):
            hap = data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j]
            if hap > maximum:
                maximum = hap


def three():
    global maximum
    for i in range(N-1):
        for j in range(M-2):
            hap1 = data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i + 1][j]
            hap2 = data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i + 1][j + 1]
            hap3 = data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i + 1][j + 2]
            hap = max(hap1, hap2, hap3)
            if hap > maximum:
                maximum = hap
    for j in range(M-1):
        for i in range(N-2):
            hap1 = data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i][j + 1]
            hap2 = data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i + 1][j + 1]
            hap3 = data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i + 2][j + 1]
            hap = max(hap1, hap2, hap3)
            if hap > maximum:
                maximum = hap


def two():
    global maximum
    for i in range(N-1):
        for j in range(M-1):
            hap = data[i][j] + data[i+1][j] + data[i][j+1] + data[i+1][j+1]
            if hap > maximum:
                maximum = hap
    for i in range(N-1):
        for j in range(1, M-1):
            hap1 = data[i][j] + data[i][j + 1] + data[i + 1][j] + data[i + 1][j - 1]
            hap2 = data[i][j] + data[i][j - 1] + data[i + 1][j] + data[i + 1][j + 1]
            hap = max(hap1, hap2)
            if hap > maximum:
                maximum = hap
    for j in range(M-1):
        for i in range(1, N-1):
            hap1 = data[i][j] + data[i+1][j] + data[i][j+1] + data[i-1][j+1]
            hap2 = data[i][j] + data[i][j+1] + data[i-1][j] + data[i+1][j+1]
            hap = max(hap1, hap2)
            if hap > maximum:
                maximum = hap


def one():
    global maximum
    for i in range(1, N):
        for j in range(M-2):
            hap1 = data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i - 1][j]
            hap2 = data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i - 1][j + 1]
            hap3 = data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i - 1][j + 2]
            hap = max(hap1, hap2, hap3)
            if hap > maximum:
                maximum = hap
    for j in range(1, M):
        for i in range(N-2):
            hap1 = data[i][j] + data[i+1][j] + data[i+2][j] + data[i][j-1]
            hap2 = data[i][j] + data[i+1][j] + data[i+2][j] + data[i + 1][j - 1]
            hap3 = data[i][j] + data[i+1][j] + data[i+2][j] + data[i + 2][j - 1]
            hap = max(hap1, hap2, hap3)
            if hap > maximum:
                maximum = hap


N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

maximum = 0
four()
three()
two()
one()
print(maximum)
