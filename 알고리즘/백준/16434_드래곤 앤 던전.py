import sys
sys.stdin = open('16434_드래곤 앤 던전.txt')
input = sys.stdin.readline


def find_HP(start, end):
    while start < end:
        mid = (start+end)//2
        hp = mid
        atk = A
        flag = 0
        for room in rooms:
            if room[0] == 1: # 몬스터
                if room[2] % atk == 0:
                    if hp - (room[2]//atk-1) * room[1] > 0:
                        hp -= (room[2]//atk-1) * room[1]
                    else:
                        flag = -1
                        break
                else:
                    if hp - (room[2]//atk)*room[1] > 0:
                        hp -= (room[2]//atk)*room[1]
                    else:
                        flag = -1
                        break
            else: # 포션
                atk += room[1]
                hp = min(mid, hp + room[2])
        if flag == -1:
            start = mid + 1
        else:
            end = mid
    return end


N, A = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]
print(find_HP(1, 123456*1000000*1000000))
