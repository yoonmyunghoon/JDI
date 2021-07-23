import sys
sys.stdin = open("2211_네트워크 복구.txt")
# input = sys.stdin.readline

'''
1번이 슈퍼 컴퓨터
통신은 완전쌍방향 방식
모든 컴퓨터들은 이어져있어야함
슈퍼컴퓨터와 통신하는데 걸리는 시간을 최소로 해야함
각 컴퓨터들에 대해서 슈퍼컴퓨터와 통신 시간을 최소로하도록 경로를 만들어줘야함
'''

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    A, B, C = map(int, input().split())
    G[A].append([B, C])

print(N, M)
for i in G:
    print(i)
print()

