import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    n = list(input())
    stack = []
    for i in range(len(n)):
        if len(stack) == 0:
            stack.append(n[i])
        else:
            if stack[-1] == n[i]:
                stack.pop()
            else:
                stack.append(n[i])
    print('#{} {}'.format(tc, len(stack)))
