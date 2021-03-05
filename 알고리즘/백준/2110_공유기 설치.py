import sys
sys.stdin = open('2110_공유기 설치.txt')
input = sys.stdin.readline


def find_distance(start, end):
    while start <= end:
        mid = (start+end)//2
        cnt = 1
        left_house = house_list[0]
        for i in range(house_len):
            if house_list[i] - left_house >= mid:
                cnt += 1
                left_house = house_list[i]
        if cnt < C:
            end = mid-1
        else:
            start = mid+1
    return end


N, C = map(int, input().split())
house_list = [int(input()) for _  in range(N)]
house_list.sort()
house_len = len(house_list)
print(find_distance(1, house_list[-1]-house_list[0]))
