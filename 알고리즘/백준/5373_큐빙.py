import sys
sys.stdin = open("5373_큐빙.txt")

def T_d(x_side):
    tmp = x_side[0][0]
    x_side[0][0] = x_side[2][0]
    x_side[2][0] = x_side[2][2]
    x_side[2][2] = x_side[0][2]
    x_side[0][2] = tmp
    tmp1 = x_side[0][1]
    x_side[0][1] = x_side[1][0]
    x_side[1][0] = x_side[2][1]
    x_side[2][1] = x_side[1][2]
    x_side[1][2] = tmp1

def DT_d(x_side):
    tmp = x_side[0][0]
    x_side[0][0] = x_side[0][2]
    x_side[0][2] = x_side[2][2]
    x_side[2][2] = x_side[2][0]
    x_side[2][0] = tmp
    tmp1 = x_side[0][1]
    x_side[0][1] = x_side[1][2]
    x_side[1][2] = x_side[2][1]
    x_side[2][1] = x_side[1][0]
    x_side[1][0] = tmp1

def U_change(d):
    if d == '+':
        T_d(u_side)
        tmp = f_side[0]
        f_side[0] = r_side[0]
        r_side[0] = b_side[0]
        b_side[0] = l_side[0]
        l_side[0] = tmp
    else:
        DT_d(u_side)
        tmp = f_side[0]
        f_side[0] = l_side[0]
        l_side[0] = b_side[0]
        b_side[0] = r_side[0]
        r_side[0] = tmp

def F_change(d):
    if d == '+':
        T_d(f_side)
        tmp1, tmp2, tmp3 = u_side[2][0], u_side[2][1], u_side[2][2]
        u_side[2][0], u_side[2][1], u_side[2][2] = l_side[2][2], l_side[1][2], l_side[0][2]
        l_side[2][2], l_side[1][2], l_side[0][2] = d_side[0][2], d_side[0][1], d_side[0][0]
        d_side[0][2], d_side[0][1], d_side[0][0] = r_side[0][0], r_side[1][0], r_side[2][0]
        r_side[0][0], r_side[1][0], r_side[2][0] = tmp1, tmp2, tmp3
    else:
        DT_d(f_side)
        tmp1, tmp2, tmp3 = u_side[2][0], u_side[2][1], u_side[2][2]
        u_side[2][0], u_side[2][1], u_side[2][2] = r_side[0][0], r_side[1][0], r_side[2][0]
        r_side[0][0], r_side[1][0], r_side[2][0] = d_side[0][2], d_side[0][1], d_side[0][0]
        d_side[0][2], d_side[0][1], d_side[0][0] = l_side[2][2], l_side[1][2], l_side[0][2]
        l_side[2][2], l_side[1][2], l_side[0][2] = tmp1, tmp2, tmp3

def D_change(d):
    if d == '+':
        T_d(d_side)
        tmp = f_side[2]
        f_side[2] = l_side[2]
        l_side[2] = b_side[2]
        b_side[2] = r_side[2]
        r_side[2] = tmp
    else:
        DT_d(d_side)
        tmp = f_side[2]
        f_side[2] = r_side[2]
        r_side[2] = b_side[2]
        b_side[2] = l_side[2]
        l_side[2] = tmp

def B_change(d):
    if d == '+':
        T_d(b_side)
        tmp1, tmp2, tmp3 = u_side[0][0], u_side[0][1], u_side[0][2]
        u_side[0][0], u_side[0][1], u_side[0][2] = r_side[0][2], r_side[1][2], r_side[2][2]
        r_side[0][2], r_side[1][2], r_side[2][2] = d_side[2][2], d_side[2][1], d_side[2][0]
        d_side[2][2], d_side[2][1], d_side[2][0] = l_side[2][0], l_side[1][0], l_side[0][0]
        l_side[2][0], l_side[1][0], l_side[0][0] = tmp1, tmp2, tmp3
    else:
        DT_d(b_side)
        tmp1, tmp2, tmp3 = u_side[0][0], u_side[0][1], u_side[0][2]
        u_side[0][0], u_side[0][1], u_side[0][2] = l_side[2][0], l_side[1][0], l_side[0][0]
        l_side[2][0], l_side[1][0], l_side[0][0] = d_side[2][2], d_side[2][1], d_side[2][0]
        d_side[2][2], d_side[2][1], d_side[2][0] = r_side[0][2], r_side[1][2], r_side[2][2]
        r_side[0][2], r_side[1][2], r_side[2][2] = tmp1, tmp2, tmp3

def L_change(d):
    if d == '+':
        T_d(l_side)
        tmp1, tmp2, tmp3 = u_side[0][0], u_side[1][0], u_side[2][0]
        u_side[0][0], u_side[1][0], u_side[2][0] = b_side[2][2], b_side[1][2], b_side[0][2]
        b_side[2][2], b_side[1][2], b_side[0][2] = d_side[0][0], d_side[1][0], d_side[2][0]
        d_side[0][0], d_side[1][0], d_side[2][0] = f_side[0][0], f_side[1][0], f_side[2][0]
        f_side[0][0], f_side[1][0], f_side[2][0] = tmp1, tmp2, tmp3
    else:
        DT_d(l_side)
        tmp1, tmp2, tmp3 = u_side[0][0], u_side[1][0], u_side[2][0]
        u_side[0][0], u_side[1][0], u_side[2][0] = f_side[0][0], f_side[1][0], f_side[2][0]
        f_side[0][0], f_side[1][0], f_side[2][0] = d_side[0][0], d_side[1][0], d_side[2][0]
        d_side[0][0], d_side[1][0], d_side[2][0] = b_side[2][2], b_side[1][2], b_side[0][2]
        b_side[2][2], b_side[1][2], b_side[0][2] = tmp1, tmp2, tmp3

def R_change(d):
    if d == '+':
        T_d(r_side)
        tmp1, tmp2, tmp3 = u_side[0][2], u_side[1][2], u_side[2][2]
        u_side[0][2], u_side[1][2], u_side[2][2] = f_side[0][2], f_side[1][2], f_side[2][2]
        f_side[0][2], f_side[1][2], f_side[2][2] = d_side[0][2], d_side[1][2], d_side[2][2]
        d_side[0][2], d_side[1][2], d_side[2][2] = b_side[2][0], b_side[1][0], b_side[0][0]
        b_side[2][0], b_side[1][0], b_side[0][0] = tmp1, tmp2, tmp3
    else:
        DT_d(r_side)
        tmp1, tmp2, tmp3 = u_side[0][2], u_side[1][2], u_side[2][2]
        u_side[0][2], u_side[1][2], u_side[2][2] = b_side[2][0], b_side[1][0], b_side[0][0]
        b_side[2][0], b_side[1][0], b_side[0][0] = d_side[0][2], d_side[1][2], d_side[2][2]
        d_side[0][2], d_side[1][2], d_side[2][2] = f_side[0][2], f_side[1][2], f_side[2][2]
        f_side[0][2], f_side[1][2], f_side[2][2] = tmp1, tmp2, tmp3


T = int(input())
for tc in range(1, T+1):
    u_side = [['w', 'w', 'w'],
              ['w', 'w', 'w'],
              ['w', 'w', 'w']]

    f_side = [['r', 'r', 'r'],
              ['r', 'r', 'r'],
              ['r', 'r', 'r']]

    d_side = [['y', 'y', 'y'],
              ['y', 'y', 'y'],
              ['y', 'y', 'y']]

    b_side = [['o', 'o', 'o'],
              ['o', 'o', 'o'],
              ['o', 'o', 'o']]

    l_side = [['g', 'g', 'g'],
              ['g', 'g', 'g'],
              ['g', 'g', 'g']]

    r_side = [['b', 'b', 'b'],
              ['b', 'b', 'b'],
              ['b', 'b', 'b']]

    n = int(input())
    info = list(input().split())

    for i in range(n):
        if info[i][0] == 'U': U_change(info[i][1])
        elif info[i][0] == 'F': F_change(info[i][1])
        elif info[i][0] == 'D': D_change(info[i][1])
        elif info[i][0] == 'B': B_change(info[i][1])
        elif info[i][0] == 'L': L_change(info[i][1])
        elif info[i][0] == 'R': R_change(info[i][1])

    for i in range(3):
        for j in range(3):
            print(u_side[i][j], end='')
        print()


