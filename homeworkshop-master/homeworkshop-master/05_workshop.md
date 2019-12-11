# 05_workshop

## 01_문제

```calc.py
def plus(a, b):
    p = a + b
    return p

def minus(a, b):
    m = a - b
    return m

def multiple(a, b):
    k = a * b
    return k

def division(a, b):
    try:
        n = a / b
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'
    else:
        return n

```

## 02_문제

```python
import calc
n1 = int(input())
n2 = int(input())
print(calc.plus(n1,n2))
print(calc.minus(n1,n2))
print(calc.mulitple(n1,n2))
print(calc.division(n1,n2))
```

![](images/module.PNG)

