import requests
import json
import pprint
import random

scom = ['not', 'up', 'right', 'down', 'left', 'in', 'out']
dr = [0, -1, 0, 1, 0, 0, 0]
dc = [0, 0, 1, 0, -1, 0, 0]
tcommand = {scom[i]: i for i in range(7)}


class Truck:
    def __init__(self):
        self.p = 0
        self.load = 0

    def __str__(self):
        return str(self.p)+' '+str(self.load)

    def __repr__(self):
        return '('+str(self.p)+' '+str(self.load)+')'


def start(url, qid):
    path = 'start'
    token = ''
    param = {'problem': qid}
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
    req = requests.post('/'.join([url, path]), headers=headers, data=json.dumps(param))
    result = req.json()
    return result


def get_locations(url, headers, bycycle):
    path = 'locations'
    req = requests.get('/'.join([url, path]), headers=headers)
    result = req.json()

    for id, cnt in [(i['id'], i['located_bikes_count']) for i in result['locations']]:
        bycycle[id] = cnt

    return bycycle


def get_trucks(url, headers, trucks):
    path = 'trucks'
    req = requests.get('/'.join([url, path]), headers=headers)
    result = req.json()

    for id, p, cnt in [(i['id'], i['location_id'], i['loaded_bikes_count']) for i in result['trucks']]:
        trucks[id].p = p
        trucks[id].load = cnt

    return result


def simulate(url, headers, data):
    path = 'simulate'
    req = requests.put('/'.join([url, path]), headers=headers, data=data)
    result = req.json()

    return result

url = ''
qid = 1
auth_key = start(url, qid)['auth_key']
headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}

if qid == 1:
    msize = 5
    mean = 2
else:
    msize = 60
    mean = 3

mymap = [[((msize-i-1)+msize*j) for j in range(msize)] for i in range(msize)]
pos = dict()
for i in range(msize):
    for j in range(msize):
        pos[mymap[i][j]] = (i, j)
bycycles = [0 for i in range(msize*msize)]
tnum = [0, 5, 10]
trucks = [Truck() for i in range(tnum[qid])]
next_command = [[] for _ in range(len(trucks))]
bnum = [0, 4, 3]
prev_bycycle = [bnum[qid] for i in range(msize*msize)]

for i in range(720):
    trucksdes = [int(random.uniform(0, msize*msize)) for _ in range(len(trucks))]
    bycycles = get_locations(url, headers, bycycles)




