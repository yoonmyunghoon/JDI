# 02_workshop

## 01_문제

```python
n = 5
m = 9
for i in range(m):
    for j in range(n):
        print('*', end='')
    print('')
```

## 02_문제

```python
student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
sum = 0
average = 0
for value in student.values():
    sum = sum + value
average = sum/len(student) 
print(average)
```

## 03_문제

```python
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
blood_dict = {}
for b in blood_types:
    if blood_dict.get(b):
        blood_dict[b] += 1
    else:
        blood_dict[b] = 1
print(blood_dict)
```

