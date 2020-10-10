def solution(p,n):
    am_pm = p[:2]
    h = p[3:5]
    m = p[6:8]
    s = p[9:11]
    if am_pm == 'PM':
        if h != '12':
            h = str(int(h) + 12)
    else:
        if h == '12':
            h = '00'
    add_h = 0
    add_m = 0
    add_s = 0
    if n < 60:
        add_s = n
    else:
        add_s = n % 60
        n = n // 60
        if n < 60:
            add_m = n
        else:
            add_m = n % 60
            n = n // 60
            n = n % 24
            add_h = n
    if int(s) + add_s >= 60:
        result_s = int(s) + add_s - 60
        add_m += 1
    else:
        result_s = int(s) + add_s
    if int(m) + add_m >= 60:
        result_m = int(m) + add_m - 60
        add_h += 1
    else:
        result_m = int(m) + add_m
    if int(h) + add_h >= 24:
        result_h = int(h) + add_h - 24
    else:
        result_h = int(h) + add_h
    answer = ""
    if result_h >= 10:
        answer += str(result_h) + ':'
    else:
        answer += '0' + str(result_h) + ':'
    if result_m >= 10:
        answer += str(result_m) + ':'
    else:
        answer += '0' + str(result_m) + ':'
    if result_s >= 10:
        answer += str(result_s)
    else:
        answer += '0' + str(result_s)
    return answer

P = "PM 01:00:00"
N = 10
print(solution(P, N))