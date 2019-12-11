# 04_workshop

## 01_문제

```python
import math
n = float(input())
def my_sqrt(n):
    a = 1
    b = n
    while math.isclose(a**2, n) == False:
        if a**2 <= n < b**2:
            if n <= ((a+b)/2)**2 < b**2:
                b = (a+b)/2
            else:
                a = (a+b)/2
    return a, b

print(my_sqrt(n))


```



```python
def my_sqrt(n):
    x, y = 1, n # 양의 정수 -> 1 ~ n
    result = 1 # 우리가 추측하는 제곱근의 근사값

    # while not math.isclose(result ** 2, n):
    while abs(result**2 - n) > 0.0000000001:
        # 제곱근 제곱과 입력 값의 차이가 적어도 0.000000001보다 작아지면 
        # 그 차이가 거의 없다고 봄

        result = (x + y) / 2
        # 양쪽 끝 값의 절반을 다시 제곱근의 근사치로 둠

        if result ** 2 < n:
            x = result
        else:
            y = result

    return result

print(my_sqrt(9))
```

