def solution(people, limit):
    people.sort()
    cnt = 0
    s = 0
    e = len(people) - 1
    while 1:
        if s == e:
            cnt += 1
            break
        if s > e:
            break
        if people[s] + people[e] > limit:
            cnt += 1
            e -= 1
        else:
            cnt += 1
            s += 1
            e -= 1
    return cnt


ex_people = [70, 80, 50]
ex_limit = 100
print(solution(ex_people, ex_limit))