def solution(k, room_number):
    full = []
    answer = []
    for n in room_number:
        if n not in full:
            full.append(n)
            answer.append(n)
        else:
            c = n + 1
            while 1:
                if c not in full:
                    full.append(c)
                    answer.append(c)
                    break
                else:
                    c += 1
    return answer

k = 10
room_number = [1,3,4,1,3,1]
print(solution(k, room_number))