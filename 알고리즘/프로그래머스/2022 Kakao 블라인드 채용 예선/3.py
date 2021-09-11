import math


def solution(fees, records):

    def cal_time(start_time, end_time):
        start_h, start_m = start_time.split(':')
        end_h, end_m = end_time.split(':')
        start_time_m = 60*int(start_h) + int(start_m)
        end_time_m = 60*int(end_h) + int(end_m)
        return end_time_m - start_time_m

    def cal_fee(t):
        if t <= fees[0]:
            return fees[1]
        else:
            t = t - fees[0]
            return fees[1] + math.ceil(t/fees[2])*fees[3]

    history_dict = {}
    time_dict = {}

    for record in records:
        time, car_number, act = record.split(' ')
        if act == 'IN':
            history_dict[car_number] = time
            if car_number not in time_dict:
                time_dict[car_number] = 0
        else:
            # 시간 구하기
            time_diff = cal_time(history_dict[car_number], time)
            time_dict[car_number] += time_diff
            history_dict[car_number] = 'empty'
    for k, v in history_dict.items():
        if v != 'empty':
            time_diff = cal_time(v, '23:59')
            time_dict[k] += time_diff
            history_dict[k] = 'empty'
    result = []
    for k, v in time_dict.items():
        result.append([k, cal_fee(v)])
    result.sort()
    answer = list(map(lambda x: x[1], result))
    return answer


fees_ex = [180, 5000, 10, 600]
records_ex = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees_ex, records_ex))