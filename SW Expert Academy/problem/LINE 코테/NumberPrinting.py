import sys
sys.stdin = open("NumberPrinting.txt")

def num0(n):
    for i in range(2*n-1):
        for j in range(n):
            if i == 0 or i == 2*n-2:
                print('#', end='')
            else:
                if j == n-1 or j == 0:
                    print('#', end='')
                else:
                    print('.', end='')
        print()
def num1(n):
    for i in range(2*n-1):
        for j in range(n):
            if j == n-1:
                print('#', end='')
            else:
                print('.', end='')
        print()
def num2(n):
    for i in range(2*n-1):
        for j in range(n):
            if i == 0 or i == 2*n-2 or i == n-1:
                print('#', end='')
            if 0 < i < n-1:
                if j == n-1:
                    print('#', end='')
                else:
                    print('.', end='')
            if n-1 < i < 2*n-2:
                if j == 0:
                    print('#', end='')
                else:
                    print('.', end='')
        print()
def num3(n):
    for i in range(2*n-1):
        for j in range(n):
            if i == 0 or i == 2*n-2 or i == n-1:
                print('#', end='')
            if 0 < i < n-1:
                if j == n-1:
                    print('#', end='')
                else:
                    print('.', end='')
            if n-1 < i < 2*n-2:
                if j == n - 1:
                    print('#', end='')
                else:
                    print('.', end='')
        print()
def num4(n):
    for i in range(2*n-1):
        for j in range(n):
            if 0 <= i < n-1:
                if j == n-1 or j == 0:
                    print('#', end='')
                else:
                    print('.', end='')
            if i == n-1:
                print('#', end='')
            if n-1 < i <= 2*n-2:
                if j == n - 1:
                    print('#', end='')
                else:
                    print('.', end='')
        print()
def num5(n):
    for i in range(2*n-1):
        for j in range(n):
            if i == 0 or i == 2*n-2 or i == n-1:
                print('#', end='')
            if n-1 < i < 2*n-2:
                if j == n-1:
                    print('#', end='')
                else:
                    print('.', end='')
            if 0 < i < n - 1:
                if j == 0:
                    print('#', end='')
                else:
                    print('.', end='')
        print()
def num6(n):
    for i in range(2*n-1):
        for j in range(n):
            if 0 <= i < n - 1:
                if j == 0:
                    print('#', end='')
                else:
                    print('.', end='')
            if i == n - 1 or i == 2*n-2:
                print('#', end='')
            if n - 1 < i < 2 * n - 2:
                if j == n - 1 or j == 0:
                    print('#', end='')
                else:
                    print('.', end='')
        print()
def num7(n):
    for i in range(2*n-1):
        for j in range(n):
            if i == 0:
                print('#', end='')
            else:
                if j == n-1:
                    print('#', end='')
                else:
                    print('.', end='')
        print()
def num8(n):
    for i in range(2*n-1):
        for j in range(n):
            if i == 0 or i == 2*n-2 or i == n-1:
                print('#', end='')
            if 0 < i < n-1:
                if j == n-1 or j == 0:
                    print('#', end='')
                else:
                    print('.', end='')
            if n-1 < i < 2*n-2:
                if j == n - 1 or j == 0:
                    print('#', end='')
                else:
                    print('.', end='')
        print()
def num9(n):
    for i in range(2*n-1):
        for j in range(n):
            if i == 0:
                print('#', end='')
            if 0 < i < n-1:
                if j == n-1 or j == 0:
                    print('#', end='')
                else:
                    print('.', end='')
            if i == n-1:
                print('#', end='')
            if n-1 < i <= 2*n-2:
                if j == n - 1:
                    print('#', end='')
                else:
                    print('.', end='')
        print()
N, arrange = map(str, input().split())
N = int(N)
lengths = []
numbers = []
for i in range(N):
    a, b = map(str, input().split())
    lengths.append(int(a))
    numbers.append(b)
for i in range(N):
    for j in range(len(numbers[i])):
        if numbers[i][j] == '0':
            num0(lengths[i])
        if numbers[i][j] == '1':
            num1(lengths[i])
        if numbers[i][j] == '2':
            num2(lengths[i])
        if numbers[i][j] == '3':
            num3(lengths[i])
        if numbers[i][j] == '4':
            num4(lengths[i])
        if numbers[i][j] == '5':
            num5(lengths[i])
        if numbers[i][j] == '6':
            num6(lengths[i])
        if numbers[i][j] == '7':
            num7(lengths[i])
        if numbers[i][j] == '8':
            num8(lengths[i])
        if numbers[i][j] == '9':
            num9(lengths[i])

