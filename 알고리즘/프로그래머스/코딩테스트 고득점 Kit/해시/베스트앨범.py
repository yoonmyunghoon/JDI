def solution(genres, plays):
    answer = []
    dict_genres = {}
    dict_plays = {}
    length = len(genres)

    for i in range(length):
        if genres[i] in dict_genres:
            dict_genres[genres[i]] += plays[i]
            dict_plays[genres[i]].append([plays[i], i])
        else:
            dict_genres[genres[i]] = plays[i]
            dict_plays[genres[i]] = [[plays[i], i]]

    for k, v in dict_plays.items():
        dict_plays[k].sort(key=lambda x: (-x[0], x[1]))

    list_genres = sorted(dict_genres.items(), key=lambda x: -x[1])
    for i in range(len(list_genres)):
        temp = dict_plays[list_genres[i][0]]
        if len(temp) >= 2:
            answer.append(temp[0][1])
            answer.append(temp[1][1])
        else:
            answer.append(temp[0][1])
    return answer