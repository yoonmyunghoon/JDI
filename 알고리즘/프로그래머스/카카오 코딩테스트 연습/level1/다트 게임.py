def solution(dart_result):
    answer = 0
    calculator = [[1 for _ in range(3)] for _ in range(4)]
    index = -1
    number = ''
    for c in dart_result:
        if c in 'SDT':
            index += 1
            calculator[0][index] *= int(number)
            if c == 'S':
                calculator[1][index] *= 1
            elif c == 'D':
                calculator[1][index] *= 2
            else:
                calculator[1][index] *= 3
            number = ''
        elif c in '*':
            calculator[2][index] *= 2
            if index != 0:
                calculator[2][index-1] *= 2
        elif c == '#':
            calculator[3][index] *= -1
        else:
            number += c
    for i in range(3):
        num = calculator[0][i]
        answer += (num**(calculator[1][i]))*(calculator[2][i])*(calculator[3][i])
    return answer


dart_result_ex = '1D2S3T*'
print(solution(dart_result_ex))
