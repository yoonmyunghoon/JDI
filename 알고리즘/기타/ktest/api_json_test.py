import requests
import json


def start_request(url, qid):
    path = 'start'
    token = ''
    param = {'problem': qid}
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
    req = requests.post('/'.join([url, path]), headers=headers, data=json.dumps(param))
    result = req.json()
    return result


def get_request(url, headers):
    path = 'get'
    req = requests.get('/'.join([url, path]), headers=headers)
    result = req.json()
    return result


def post_request(url, headers, data):
    path = 'post'
    result = requests.post('/'.join([url, path]), headers=headers, data=data)
    return result


def put_request(url, headers, data):
    path = 'put'
    result = requests.put('/'.join([url, path]), headers=headers, data=data)
    return result


base_url = ''
auth_key = start_request(base_url, 1)['auth_key']
base_headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}