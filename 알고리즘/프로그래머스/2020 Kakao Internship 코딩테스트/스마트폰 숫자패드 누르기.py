def cal_d(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solution(numbers, hand):
    keypad = [(3,1),
              (0,0),(0,1),(0,2),
              (1,0),(1,1),(1,2),
              (2,0),(2,1),(2,2)
              ]
    result = []
    last_l = (3,0)
    last_r = (3,2)
    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            result.append('L')
            last_l = keypad[numbers[i]]
        elif numbers[i] in [3, 6, 9]:
            result.append('R')
            last_r = keypad[numbers[i]]
        else:
            if cal_d(keypad[numbers[i]], last_l) < cal_d(keypad[numbers[i]], last_r):
                result.append('L')
                last_l = keypad[numbers[i]]
            elif cal_d(keypad[numbers[i]], last_l) > cal_d(keypad[numbers[i]], last_r):
                result.append('R')
                last_r = keypad[numbers[i]]
            else:
                if hand == "left":
                    result.append('L')
                    last_l = keypad[numbers[i]]
                else:
                    result.append('R')
                    last_r = keypad[numbers[i]]

    return ''.join(result)


numbers = [
    [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],
    [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
]
hand = [
    "right",
    "left",
    "right"
]

for i in range(len(hand)):
    print(solution(numbers[i], hand[i]))