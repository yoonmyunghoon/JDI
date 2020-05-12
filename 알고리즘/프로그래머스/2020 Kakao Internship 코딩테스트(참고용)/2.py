def solution(expression):
    D = {'+': 0, '-': 1, '*': 2}
    exp = expression.replace('-', ' - ')
    exp = exp.replace('+', ' + ')
    exp = exp.replace('*', ' * ')
    exp = exp.split(' ')
    priority_list = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    result = 0
    for priority in priority_list:
        equ = []
        opers = []
        for sp in exp:
            if sp in '+-*':
                while opers and priority[D[opers[-1]]] >= priority[D[sp]]:
                    equ.append(opers.pop())
                opers.append(sp)
            else:
                equ.append(sp)
        while opers:
            equ.append(opers.pop())
        st = []
        for word in equ:
            if word in '+-*':
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

solution("100-200*300-500+20")