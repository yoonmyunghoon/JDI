def solution(record):
    answer = []
    user_dict = {}
    history = []

    for notice in record:
        split_notice = notice.split(' ')
        if split_notice[0] == 'Enter':
            user_id = split_notice[1]
            user_name = split_notice[2]
            user_dict[user_id] = user_name
            history.append(['E', user_id])
        elif split_notice[0] == 'Leave':
            user_id = split_notice[1]
            history.append(['L', user_id])
        else:
            user_id = split_notice[1]
            user_name = split_notice[2]
            user_dict[user_id] = user_name
    for i in history:
        if i[0] == 'E':
            answer.append(user_dict[i[1]] + "님이 들어왔습니다.")
        else:
            answer.append(user_dict[i[1]] + "님이 나갔습니다.")
    return answer


record_ex = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
             ]
print(solution(record_ex))


