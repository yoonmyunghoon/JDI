
def check(s):
    stack = []
    if s[0] == ')':
        return 0
    if s[-1] == '(':
        return 0
    for i in range(len(s)):
        if s[i] == ')':
            if len(stack) == 0:
                return 0
            else:
                stack.pop()
        else:
            stack.append('(')
    if len(stack) == 0:
        return 1
    else:
        return 0


def change(s):
    ns = ''
    for i in range(1, len(s)-1):
        if s[i] == ')':
            ns += '('
        else:
            ns += ')'
    return ns


def recursion(p):
    if p == '':
        return ''
    cnt1 = 0
    cnt2 = 0
    point = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            point = i
            break
    u = p[:point+1]
    v = p[point+1:]
    if check(u):
        return u + recursion(v)
    else:
        return '(' + recursion(v) + ')' + change(u)


def solution(p):
    if check(p):
        return p
    else:
        answer = recursion(p)
        return answer


print(solution("()(())()"))