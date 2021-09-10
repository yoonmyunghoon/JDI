from itertools import permutations


def solution(expression):
    expression_list = []
    used_operators = set()
    c = ''
    for i in expression:
        if i in '+-*':
            used_operators.add(i)
            expression_list.append(int(c))
            expression_list.append(i)
            c = ''
        else:
            c += i
    expression_list.append(int(c))
    used_operators = list(used_operators)
    result = 0
    priority_list = list(permutations(used_operators))
    for priority in priority_list:
        operator_dict = {}
        for k in range(len(priority)):
            operator_dict[priority[k]] = k
        cal_stack = []
        operator_stack = []
        for e in expression_list:
            if isinstance(e, int):
                cal_stack.append(e)
            else:
                while 1:
                    if operator_stack:
                        a = operator_stack[-1]
                        if operator_dict[a] >= operator_dict[e]:
                            a = operator_stack.pop()
                            cal_stack.append(a)
                        else:
                            operator_stack.append(e)
                            break
                    else:
                        operator_stack.append(e)
                        break
        while operator_stack:
            cal_stack.append(operator_stack.pop())
        st = []
        for word in cal_stack:
            if isinstance(word, str):
                tmp = st.pop()
                if word == '+':
                    st[-1] += tmp
                elif word == '-':
                    st[-1] -= tmp
                else:
                    st[-1] *= tmp
            else:
                st.append(int(word))
        result = max(result, abs(st[0]))
    return result


expression_ex = "100-200*300-500+20"
print(solution(expression_ex))
