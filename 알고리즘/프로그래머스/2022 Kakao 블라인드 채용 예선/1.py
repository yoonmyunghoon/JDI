def solution(id_list, report, k):
    answer = []
    count_dict = {}
    user_dict = {}
    report = list(set(report))
    for user in id_list:
        user_dict[user] = set()
        count_dict[user] = 0
    for data in report:
        user1, user2 = data.split(' ')
        user_dict[user1].add(user2)
        count_dict[user2] += 1
    reported_users = []
    for key, value in count_dict.items():
        if value >= k:
            reported_users.append(key)
    for key, value in user_dict.items():
        cnt = 0
        for reported_user in reported_users:
            if reported_user in value:
                cnt += 1
        answer.append(cnt)
    return answer


id_list_ex = ["con", "ryan"]
report_ex = ["ryan con", "ryan con", "ryan con", "ryan con"]
k_ex = 3
print(solution(id_list_ex, report_ex, k_ex))