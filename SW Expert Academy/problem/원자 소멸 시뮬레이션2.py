import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atoms = []
    confirm = [0]*N
    times = 0
    energy = 0
    for i in range(N):
        atom = list(map(int, input().split()))
        atom[0] += 1000
        atom[0] = atom[0] * 2
        atom[1] += 1000
        atom[1] = atom[1] * 2
        atoms.append(atom)
    while 1:
        for i in range(N):
            if confirm[i] == 0:
                if atoms[i][0] < 0 or atoms[i][0] > 4000 or atoms[i][1] < 0 or atoms[i][1] > 4000:
                    confirm[i] = 2
        if confirm.count(0) == 0:
            break
        if times >= 4000:
            break
        times += 1
        for i in range(N):
            if confirm[i] == 0:
                if atoms[i][2] == 0:
                    atoms[i][1] += 1
                elif atoms[i][2] == 1:
                    atoms[i][1] -= 1
                elif atoms[i][2] == 2:
                    atoms[i][0] -= 1
                else:
                    atoms[i][0] += 1
        for i in range(N-1):
            if confirm[i] == 0:
                for j in range(i+1, N):
                    if confirm[j] == 0:
                        if atoms[i][0] == atoms[j][0]:
                            if atoms[i][1] == atoms[j][1]:
                                confirm[i] = 1
                                confirm[j] = 1
    for i in range(N):
        if confirm[i] == 1:
            energy += atoms[i][3]
    print('#{} {}'.format(tc, energy))
