import copy

def solution(expression):
    result = []
    start = 0
    numbers = []
    operations = []
    for i in range(len(expression)):
        if expression[i] in ['+', '-', '*']:
            numbers.append(int(expression[start:i]))
            operations.append(expression[i])
            start = i + 1
        else:
            if i == len(expression) - 1:
                numbers.append(int(expression[start:]))
    oper_types = list(set(operations))
    oper_cnt = len(oper_types)

    def perm(n, k):
        if n == k:
            operations_copy = copy.deepcopy(operations)
            numbers_copy = copy.deepcopy(numbers)
            for oper in range(len(oper_types)):
                p = 0
                while 1:
                    if oper_types[oper] not in operations_copy:
                        break
                    if oper_types[oper] == operations_copy[p]:
                        x = numbers_copy.pop(p)
                        y = numbers_copy.pop(p)
                        o = operations_copy.pop(p)
                        r = 0
                        if o == '*':
                            r = x * y
                        elif o == '+':
                            r = x + y
                        else:
                            r = x - y
                        numbers_copy.insert(p, r)
                        p = 0
                    else:
                        p += 1
                if len(numbers_copy) == 1:
                    result.append(abs(numbers_copy[0]))
        else:
            for i in range(k, n):
                oper_types[i], oper_types[k] = oper_types[k], oper_types[i]
                perm(n, k+1)
                oper_types[i], oper_types[k] = oper_types[k], oper_types[i]
    perm(oper_cnt, 0)

    return max(result)




expression = [
    "100-200*300-500+20",
    "50*6-3*2"
]

for i in range(len(expression)):
    print(solution(expression[i]))