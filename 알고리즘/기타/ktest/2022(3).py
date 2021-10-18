import requests
import json
import pprint


# ------ API 정의 -------

def start(url, qid):
    '''
    {
      "auth_key": "",
      "problem": 1,
      "time": 0
    }
    '''
    path = 'start'
    token = ''
    param = {'problem': qid}
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
    req = requests.post('/'.join([url, path]), headers=headers, data=json.dumps(param))
    result = req.json()
    return result


def get_waiting_line(url, headers):
    '''
    {
      "waiting_line": [
        { "id": 1, "from": 3 },
        { "id": 2, "from": 14 },
        ...
      ]
    }
    '''
    path = 'waiting_line'
    req = requests.get('/'.join([url, path]), headers=headers)
    result = req.json()
    return result


def get_game_result(url, headers):
    '''
    {
      "game_result": [
        {"win": 10, "lose": 2, "taken": 7 },
        {"win": 7, "lose": 12, "taken": 33 },
        ...
      ]
    }
    '''
    path = 'game_result'
    req = requests.get('/'.join([url, path]), headers=headers)
    result = req.json()
    return result


def get_user_info(url, headers):
    '''
    {
      "user_info": [
        { "id": 1, "grade": 2100 },
        { "id": 13, "grade": 1501 },
        ...
      ]
    }
    '''
    path = 'user_info'
    req = requests.get('/'.join([url, path]), headers=headers)
    result = req.json()
    return result


def match(url, headers, pairs):
    '''
    {
      "status": "ready",
      "time": 312
    }
    '''
    path = 'match'
    param = {'pairs': pairs}    # "pairs": [[1, 2], [9, 7], [11, 49]]
    req = requests.put('/'.join([url, path]), headers=headers, data=json.dumps(param))
    result = req.json()
    return result


def change_grade(url, headers, commands):
    '''
    {
      "status": "ready"
    }
    '''
    path = 'change_grade'
    param = {'commands': commands}    # "commands": [{ "id": 1, "grade": 1900 }...]
    req = requests.put('/'.join([url, path]), headers=headers, data=json.dumps(param))
    result = req.json()
    return result


def get_score(url, headers):
    '''
    {
      "status": "finished",
      "efficiency_score": -1.0,
      "accuracy_score1": 0.0,
      "accuracy_score2": 32.62,
      "score": 30.94
    }
    '''
    path = 'score'
    req = requests.get('/'.join([url, path]), headers=headers)
    result = req.json()
    return result


# ------- 필요한 함수 정의 -------

# grade 에 저장된 등급 데이터를 요청에 맞게 변경해줌
def get_commands():
    min_grade = min(grade)
    if min_grade < 0:
        new_grade_list = [old_grade - min_grade for old_grade in grade]
    else:
        new_grade_list = [old_grade for old_grade in grade]

    commands = []
    for i, e in enumerate(new_grade_list):
        if e > 9999:
            e = 9999
        user_info = {'id': i, 'grade': e}
        commands.append(user_info)
    return commands


# 대기열에 있는 user 들의 등급을 확인해서 정렬을 해줌
def ordering(waiting_line):
    user_grade = []
    result = []
    for ui in waiting_line:
        user_id = ui['id']
        user_grade.append((grade[user_id], user_id))
    user_grade.sort()
    n = 0
    # 정렬한 후, 연속하는 등급의 차이가 특정값 이하일 경우에 result 에 넣어줌
    while 1:
        if n >= len(user_grade)-1:
            break
        if abs(user_grade[n][0] - user_grade[n+1][0]) < diff:
            result.append(user_grade[n])
            result.append(user_grade[n+1])
            n += 2
        else:
            n += 1
    return result


# ------- 메인 -------
base_url = ''
qid = 1
auth_key = start(base_url, qid)['auth_key']
headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}

if qid == 1:
    user_num = 30
    m_mean = 1
    diff = 85  # 허용 등급 차이
else:
    user_num = 900
    m_mean = 45
    diff = 3000  # 허용 등급 차이

# 초기에 user 들의 등급을 받아옴
initial_user_info = get_user_info(base_url, headers)['user_info']

# grade: user 등급을 저장한 배열, id가 index
grade = [0 for _ in range(user_num+1)]
for ui in initial_user_info:
    grade[ui['id']] = ui['grade']

for turn in range(596):
    # 마지막에 등급 변경 요청
    if turn == 595:
        change_grade(base_url, headers, get_commands())

    # 대기열 확인
    waiting_line = get_waiting_line(base_url, headers)['waiting_line']
    # pprint.pprint(waiting_line)
    if len(waiting_line) < 2:
        pairs = []
        match_result = match(base_url, headers, pairs)
        pprint.pprint(match_result)
        continue

    # 매칭
    # 등급 순으로 정렬 후, 순서대로 두명씩 매칭
    pairs = []
    ordered_waiting_line = ordering(waiting_line)
    while 1:
        if len(ordered_waiting_line) < 2:
            break
        user1 = ordered_waiting_line.pop()
        user2 = ordered_waiting_line.pop()
        pairs.append([user1[1], user2[1]])
    match_result = match(base_url, headers, pairs)
    pprint.pprint(match_result)

    # 결과 확인
    game_result = get_game_result(base_url, headers)['game_result']
    pprint.pprint(game_result)
    if len(game_result) == 0:
        continue

    # 등급 수정
    for result in game_result:
        winner = result['win']
        loser = result['lose']
        time = result['taken']
        grade[winner] += (43 - time)
        grade[loser] -= (43 - time)

print(grade)
# 점수 확인
pprint.pprint(get_score(base_url, headers))




