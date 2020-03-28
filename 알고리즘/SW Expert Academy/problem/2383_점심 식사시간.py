import sys
sys.stdin = open('2383_점심 식사시간.txt')

def caldistance(people, stairs):
    return abs(people[0]-stairs[0]) + abs(people[1]-stairs[1])

def caltime(arr):
    global mintime
    time = [0, 0]
    stairs = [0, 0]
    peopletostairs0 = []
    peopletostairs1 = []
    for i in range(len(arr)):
        if arr[i] == 0:
            peopletostairs0.append(distances[i][0]+1)
        else:
            peopletostairs1.append(distances[i][1]+1)
    peopletostairs0.sort()
    peopletostairs1.sort()
    if len(peopletostairs0) > 0:
        index = 0
        while peopletostairs0.count(0) != len(peopletostairs0):
            time[0] += 1
            if stairs[0] > 0:
                for i in range(index):
                    if time[0] == peopletostairs0[i]:
                        peopletostairs0[i] = 0
                        stairs[0] -= 1
            for i in range(index, len(peopletostairs0)):
                if stairs[0] < 3:
                    if 0 < peopletostairs0[i] <= time[0]:
                        peopletostairs0[i] = time[0] + G[stairsposition[0][0]][stairsposition[0][1]]
                        stairs[0] += 1
                        index += 1

    if len(peopletostairs1) > 0:
        index = 0
        while peopletostairs1.count(0) != len(peopletostairs1):
            time[1] += 1
            if stairs[1] > 0:
                for i in range(index):
                    if time[1] == peopletostairs1[i]:
                        peopletostairs1[i] = 0
                        stairs[1] -= 1
            for i in range(index, len(peopletostairs1)):
                if stairs[1] < 3:
                    if 0 < peopletostairs1[i] <= time[1]:
                        peopletostairs1[i] = time[1] + G[stairsposition[1][0]][stairsposition[1][1]]
                        stairs[1] += 1
                        index += 1
    if mintime > max(time):
        mintime = max(time)

def powerset(n, k):
    if n == k:
        caltime(A)
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairsposition = []
    for i in range(N):
        for j in range(N):
            if G[i][j] == 1:
                people.append([i, j])
            else:
                if G[i][j] != 0:
                    stairsposition.append([i, j])

    distances = [[0]*2 for _ in range(len(people))]
    for i in range(len(people)):
        for j in range(2):
            distances[i][j] = caldistance(people[i], stairsposition[j])

    A = [0]*len(people)
    mintime = 987654321
    powerset(len(people), 0)
    print('#{} {}'.format(tc, mintime))