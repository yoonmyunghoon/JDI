import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atoms = []
    times = 0
    energy = 0
    for i in range(N):
        atom = list(map(int, input().split()))
        atom[0] += 1000
        atom[0] = atom[0]*2
        atom[1] += 1000
        atom[1] = atom[1]*2
        atoms.append(atom)
    while 1:
        p = 0
        q = 0
        n = len(atoms)
        while 1:
            if (p + q) == n:
                break
            if atoms[p][0] < 0 or atoms[p][0] > 4000 or atoms[p][1] < 0 or atoms[p][1] > 4000:
                atoms.pop(p)
                q += 1
            else:
                p += 1

        if len(atoms) == 0:
            break
        if times >= 4000:
            break
        times += 1

        for i in range(len(atoms)):
            if atoms[i][2] == 0:
                atoms[i][1] += 1
            elif atoms[i][2] == 1:
                atoms[i][1] -= 1
            elif atoms[i][2] == 2:
                atoms[i][0] -= 1
            else:
                atoms[i][0] += 1
        for i in range(len(atoms)-1):
            for j in range(i+1, len(atoms)):
                if atoms[i][0] == atoms[j][0]:
                    if atoms[i][1] == atoms[j][1]:
                        atoms[i][2] = 5
                        atoms[j][2] = 5
        k = 0
        c = 0
        n = len(atoms)
        while 1:
            if (k + c) == n:
                break
            if atoms[k][2] == 5:
                energy += atoms[k][3]
                atoms.pop(k)
                c += 1
            else:
                k += 1
    print('#{} {}'.format(tc, energy))


