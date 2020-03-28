import sys
sys.stdin = open("2960_에라토스테네스의 체.txt")

def finding():
    cnt = 0
    p = 2
    while 1:
        # 지워지지 않은 숫자 중에 가장 작은 숫자 저장
        for i in range(N - 1):
            if numbers[i] != 1:
                p = numbers[i]
                break
        # 숫자 지우는 반복문
        for i in range(N - 1):
            if numbers[i] % p == 0:
                # 이미 지워졌으면 다음으로
                if numbers[i] == 1:
                    continue
                else:
                    # cnt 추가(숫자 지우기)
                    cnt += 1
                    if cnt == K:
                        return numbers[i]
                    else:
                        numbers[i] = 1

N, K = map(int, input().split())
numbers = list(range(2, N+1))
print(finding())
