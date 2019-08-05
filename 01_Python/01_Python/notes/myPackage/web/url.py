def my_url(i=10, **api):
    if i > 10:
        return print('1~10까지의 값을 넣어주세요.')
    
    if 'key' not in api or 'targetDt' not in api:
        return print('필수 요청변수가 누락되었습니다.')
    
    str1 = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    str2 = str1 + 'itemPerPage=' + str(i) + '&'
    for key, value in api.items():
        str2 += str(key) + '=' + str(value) + '&'
    
    return str2