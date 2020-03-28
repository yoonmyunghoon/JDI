def solution(s):
    check = {}
    number = ""
    s = s[:-2]+","
    for i in s:
        if i != "{" and i != "}":
            if i != ",":
                number += i
            else:
                if check.get(number):
                    check[number] += 1
                else:
                    check[number] = 1
                number = ""
    check1 = []
    for k, v in check.items():
        check1.append([v, int(k)])
    check1.sort(reverse=True)
    answer = []
    for c in check1:
        answer.append(c[1])
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s1 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s2 = "{{20,111},{111}}"
s3 = "{{123}}"
s4 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))