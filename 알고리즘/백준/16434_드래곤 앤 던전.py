import sys, math
sys.stdin = open('16434_드래곤 앤 던전.txt')


def find_HP(start, end):
    while start < end:
        mid = (start+end)//2
        hp = mid
        atk = A
        flag = 0
        for room in rooms:
            if room[0] == 1: # 몬스터
                if math.ceil(room[2]//atk) >= math.ceil(hp//room[1]):
                    hp -= math.ceil(hp//room[1])
                else:
                    flag = -1
                    break
            else: # 포션
                atk += room[1]
                hp += min(mid, hp + room[2])
        print(start, mid, end)
        if flag == -1:
            start = mid + 1
        else:
            end = mid
    return end


N, A = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]
print(find_HP(1, 123456*1000000))
